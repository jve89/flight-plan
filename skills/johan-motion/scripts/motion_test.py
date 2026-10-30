#!/usr/bin/env python3
"""
motion_test.py  -  test scroll animations like a real visitor would.

Usage:
    python3 motion_test.py page.html            # or a URL
    python3 motion_test.py page.html --out results --devices desktop,mobile --speeds slow,fast

What it does, per device and scroll speed:
  1. Cold load: starts as soon as the DOM is ready, before fonts/video/images have loaded.
  2. Scrolls DOWN with the mouse wheel in small continuous steps (slow or fast).
     After passing each ScrollTrigger it waits, then checks the animation is complete.
  3. Saves screenshots at the start, middle and end of every pinned section.
  4. Scrolls back UP to the top and checks every reversible trigger is reset.
  5. Reports console errors.

Requirements: pip install playwright && python3 -m playwright install chromium
The page must expose GSAP's ScrollTrigger as window.ScrollTrigger (true for CDN builds).
Exit code 1 when any check fails.
"""
import argparse, asyncio, json, os, sys
from pathlib import Path
from playwright.async_api import async_playwright

DEVICES = {
    "desktop":  dict(width=1440, height=900,  touch=False, mobile=False),
    "tablet-l": dict(width=1180, height=820,  touch=True,  mobile=False),
    "tablet-p": dict(width=820,  height=1180, touch=True,  mobile=False),
    "mobile":   dict(width=390,  height=844,  touch=True,  mobile=True),
}
SPEEDS = {"slow": (80, 45), "fast": (170, 22)}   # (pixels per wheel step, ms between steps)

TRIGGERS_JS = """() => {
  if (!window.ScrollTrigger) return null;
  let next = ScrollTrigger.getAll().reduce((m, s) => Math.max(m, s.__mtid ?? -1), -1) + 1;
  return ScrollTrigger.getAll().map((st) => {
    if (st.__mtid === undefined) st.__mtid = next++;
    const i = st.__mtid;
    const el = st.trigger;
    const label = el ? (el.id ? '#' + el.id : (el.className && typeof el.className === 'string'
                  ? '.' + el.className.trim().split(/\\s+/)[0] : el.tagName.toLowerCase())) : 'trigger-' + i;
    const ta = (st.vars.toggleActions || 'play none none none').split(' ');
    const anim = st.animation || null;
    return { i, label, start: Math.round(st.start), end: Math.round(st.end), pin: !!st.pin,
             scrub: !!st.vars.scrub, once: !!st.vars.once, leaveBack: ta[3],
             hasAnim: !!anim, dur: anim ? anim.totalDuration() : 0,
             hasCallbacks: !!(st.vars.onUpdate || st.vars.onToggle || st.vars.toggleClass) };
  });
}"""
LIVE_JS = """(i) => { const st = ScrollTrigger.getAll().find(s => s.__mtid === i);
  return st ? { start: Math.round(st.start), end: Math.round(st.end) } : null; }"""
PROGRESS_JS = """(i) => { const st = ScrollTrigger.getAll().find(s => s.__mtid === i); if (!st) return null;
  return { anim: st.animation ? st.animation.progress() : null, st: st.progress }; }"""

async def wheel_to(page, target, step, delay):
    y = await page.evaluate("scrollY")
    direction = 1 if target > y else -1
    stuck = 0
    while (target - y) * direction > step / 2:
        await page.mouse.wheel(0, step * direction)
        await page.wait_for_timeout(delay)
        ny = await page.evaluate("scrollY")
        stuck = stuck + 1 if ny == y else 0
        y = ny
        if stuck > 25:
            break

async def run(url, device, speed, out):
    d = DEVICES[device]; step, delay = SPEEDS[speed]
    failures, notes = [], []
    async with async_playwright() as p:
        browser = await p.chromium.launch(args=["--autoplay-policy=no-user-gesture-required"])
        ctx = await browser.new_context(viewport={"width": d["width"], "height": d["height"]},
                                        has_touch=d["touch"], is_mobile=d["mobile"])
        page = await ctx.new_page()
        errors = []
        page.on("pageerror", lambda e: errors.append(str(e)))
        page.on("console", lambda m: errors.append(m.text) if m.type == "error" else None)
        await page.goto(url, wait_until="domcontentloaded")
        await page.mouse.move(d["width"] / 2, d["height"] / 2)
        await page.wait_for_timeout(250)
        # start scrolling immediately (cold load), then re-read triggers once refreshed
        await wheel_to(page, 400, step, delay)
        await page.wait_for_timeout(1500)
        await wheel_to(page, 0, step, delay)
        await page.wait_for_timeout(800)
        trig = await page.evaluate(TRIGGERS_JS)
        if trig is None:
            print("  window.ScrollTrigger not found: expose it on window to use this test.")
            await browser.close(); return ["ScrollTrigger not exposed"], errors
        shots = out / device / speed
        shots.mkdir(parents=True, exist_ok=True)
        max_y = await page.evaluate("document.documentElement.scrollHeight - innerHeight")

        # ---- DOWN ----
        for t in sorted(trig, key=lambda t: t["end"]):
            live = await page.evaluate(LIVE_JS, t["i"])   # positions can change after late loads
            if live: t.update(live)
            max_y = await page.evaluate("document.documentElement.scrollHeight - innerHeight")
            if t["pin"]:
                for tag, y in (("start", t["start"] + 10), ("mid", (t["start"] + t["end"]) // 2), ("end", t["end"] - 10)):
                    await wheel_to(page, y, step, delay)
                    await page.wait_for_timeout(700)
                    await page.screenshot(path=str(shots / f"{t['i']:02d}{t['label'].replace('#','').replace('.','')}_{tag}.png"))
            live = await page.evaluate(LIVE_JS, t["i"])
            if live: t.update(live)
            target = min(t["end"] + 120, max_y)
            await wheel_to(page, target, step, delay)
            await page.wait_for_timeout(300)
            if await page.evaluate("scrollY") < t["end"]:
                await wheel_to(page, target, step // 2, delay * 2)
            wait = 1200 if t["scrub"] else int(min(4000, max(1200, t["dur"] * 1000 + 400)))
            await page.wait_for_timeout(wait)
            pr = await page.evaluate(PROGRESS_JS, t["i"])
            if pr is None:
                continue
            if t["hasAnim"] and pr["anim"] is not None and pr["anim"] < 0.98:
                failures.append(f"{t['label']}: animation not finished after passing it (progress {pr['anim']:.2f})")
            elif not t["hasAnim"] and t["scrub"] and pr["st"] < 0.98:
                failures.append(f"{t['label']}: scroll progress {pr['st']:.2f} after passing it")
        await wheel_to(page, max_y, step, delay)
        await page.wait_for_timeout(800)
        await page.screenshot(path=str(shots / "zz_bottom.png"))

        # ---- UP ----
        await wheel_to(page, 0, step, delay)
        await page.wait_for_timeout(1800)
        for t in trig:
            reversible = t["scrub"] or t["leaveBack"] in ("reverse", "reset")
            if t["once"] or not reversible or t["start"] <= 0:
                continue
            pr = await page.evaluate(PROGRESS_JS, t["i"])
            if pr is None:
                continue
            val = pr["anim"] if (t["hasAnim"] and pr["anim"] is not None) else pr["st"]
            if val > 0.02:
                failures.append(f"{t['label']}: not reset after scrolling back to the top (progress {val:.2f})")
        await page.screenshot(path=str(shots / "zz_top_after_return.png"))
        await browser.close()
    return failures, errors

async def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("page")
    ap.add_argument("--out", default="motion-test-output")
    ap.add_argument("--devices", default=",".join(DEVICES))
    ap.add_argument("--speeds", default="slow,fast")
    a = ap.parse_args()
    url = a.page if a.page.startswith(("http://", "https://", "file://")) else Path(a.page).resolve().as_uri()
    out = Path(a.out); out.mkdir(parents=True, exist_ok=True)
    any_fail = False; report = []
    for dev in a.devices.split(","):
        for sp in a.speeds.split(","):
            fails, errs = await run(url, dev, sp, out)
            ok = not fails and not errs
            any_fail |= not ok
            print(f"{'PASS' if ok else 'FAIL'}  {dev:9} {sp:5}")
            for f in fails: print("      -", f)
            for e in errs[:5]: print("      console:", e)
            report.append({"device": dev, "speed": sp, "failures": fails, "errors": errs})
    (out / "report.json").write_text(json.dumps(report, indent=2))
    print(f"\nScreenshots and report in {out}/ . Look at the pinned-section screenshots before delivering.")
    sys.exit(1 if any_fail else 0)

if __name__ == "__main__":
    asyncio.run(main())
