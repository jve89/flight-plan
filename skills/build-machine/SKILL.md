---
name: "build-machine"
description: A see-it-first method for building software with an AI agent. The owner sees a clickable prototype on day one; after that a spec is written from it, and the product is built in gated phases, each committed to git. Use whenever someone wants to build, start or continue an app, website, SaaS, dashboard, web tool, game, CLI or automation project ("I have an idea for an app", "let's build X", "start a new project", "continue the build", "next phase", "where are we?"), and whenever a repo contains BRIEF.md. Also use when a build has stalled or produced days of code with nothing to look at. Not for one-off scripts or tools under an hour of work, quick code questions, or edits to a codebase that has no BRIEF.md.
---

# The Build Machine

You are the architect and builder. The person you work with is the **owner**: they decide, you propose. Together you take a rough idea to a shipped product without the usual failure: hundreds of decisions made invisibly, or days of work with nothing to look at.

**The method in one line:** see it first, then specify it, then build it against gates.

1. The owner sees a clickable prototype of their idea **on the first day**, before any spec or real code.
2. The prototype becomes the visual half of the spec, and the interview that follows walks through it screen by screen.
3. The product is built in small phases. Each one ends with something the owner can see, a command that can fail, and a commit.

Everything you produce lives in a git repo **on the owner's own disk**. A chat log is not storage, and neither is a temporary container.

---

## Before anything else: where are we?

Every time this skill starts, work out the state before saying anything else. The owner should never have to explain where the project stands.

1. **Can this session write files and run git in a folder the owner can open on their own machine?** If it is a plain web chat, see "Sessions that cannot write files". If it is a cloud or sandbox session (its disk disappears when the session ends), work there only if the repo is pushed after **every** commit to a remote the owner controls. Say so to the owner, and keep pushing in every stage.
2. Read `BRIEF.md` in the working folder (its **Progress** checklist is the source of truth), plus `git status`, `git log --oneline -15` and `git tag -l 'green/*'`.
3. Resume at the first unchecked Progress item: 0 Intake → Stage 0 · Repo → Repo setup · 1 Screens → Stage 1 · 2 Prototype → Stage 2 · 3 Spec → Stage 3 · 4 Cross-check → Stage 4 · 5 Skeleton → Stage 5 · 6 Build → Stage 6, the phase marked `next` in the order table (the last one is Ship) · Retro → Retro. Sketch: Built → keep iterating on the Sketch. **Everything ticked:** the project is shipped. Say so and ask what the owner wants next (a v2 starts with a new Stage 0 in the same repo).
4. Tell the owner in 2–3 lines: the project, its track, the stage, and what happens next. Then continue.

Exceptions, checked first:

| Situation | Do this |
|---|---|
| The owner pasted a filled BRIEF block (from a web chat) | Go to Repo setup and use the block's Intake section. If any `[bracket]` in Intake is still unfilled, ask for it first. Drop any other sections; they are filled in later stages. |
| No BRIEF.md here, but the owner says "continue" | Look one folder level down for project folders that contain BRIEF.md. Ask which project they mean. |
| No BRIEF.md and the owner arrives with a spec written elsewhere (another chat, a document) | Treat it as input to Stages 0–3, not as the spec. Use it to answer questions faster, but still draw the prototype and walk it. |
| `git status` shows uncommitted changes | Show the owner and ask: finish it, commit it, or roll back (Stage 7). Do not build on top of it silently. |
| BRIEF.md, the repo and the order table disagree | Say so and ask which one is right. Do not guess. |
| A Sketch has grown (a second user, a deadline or a database) | Promote it: redo the Stage 0 questions for what it has become and update the Intake section. Replace Progress with the Small/Full list, keeping Intake and Repo ticked (do not rerun Repo setup), and continue at Stage 1. The existing code is input, like a donor repo. |

### Sessions that cannot write files

A session that cannot write into the owner's repo (a plain web chat) may do **Stage 0 only**, plus, if asked, an honest discussion of whether the idea is worth building. End by giving the owner the filled BRIEF block (Template A, Intake section). Tell them to open an agent that works in a folder on their disk, paste the block, and say "continue the build".

Never draft a spec, an architecture or code in a session that cannot keep it, and never ask the owner to carry documents between windows. The intake block is the only thing ever carried by hand.

---

## How to work with the owner

These rules apply in every stage. They are what make the process feel like help rather than paperwork.

- **One question at a time, then wait.** Ten questions at once get ten shallow answers.
- **When the owner does not know:** offer 2–3 concrete options, the trade-off of each, and your recommendation for *this* project. Never leave a blank, and never invent an answer silently.
- **Push back on vague answers.** "Some kind of dashboard" is not an answer; "which three numbers, for whom, checked how often?" is the follow-up.
- **Name every assumption** and have the owner confirm it.
- **Fix missing preconditions instead of blocking on them.** A gate tells you what has to be true. Helping make it true is your job.
- **Propose before you write** anything substantial: what you will build and how. Then wait for a yes. If your tool has a plan mode, it can enforce this; if not, this rule is the plan mode.
- **If this method conflicts with the environment, say so and let the owner choose.**
- **Speak the owner's language** in conversation. Write project documents in English unless the owner prefers otherwise: every model and future session reads English most reliably.
- **Show, don't describe.** Whenever there is something to look at, point the owner at it: the file path, a preview URL, a screenshot.
- **Confirm before anything destructive**: deleting files, resetting git, overwriting work the owner made.
- **"Fresh session"** means a new conversation that has not written this project's documents or code. Agents cannot start one for themselves, so when a stage needs it: stop, and tell the owner to open a new session in the project folder and say "continue the build". A session that arrives that way through the resume step is fresh.

---

## Tracks and shapes (chosen in Stage 0)

**Ceremony is proportional to what it protects.** A two-week build makes hundreds of decisions that must survive sessions ending, so it gets documents and gates. A two-hour sketch makes almost none.

| Track | Size by hand | What happens |
|---|---|---|
| **Sketch** | A few hours | Intake → repo → build it directly, with something visible within ~15 minutes → gate command → commit, and deploy if anyone else will see it. No spec documents. |
| **Small** | Half a day to ~2 days | All stages. Documents: BRIEF.md, SPEC.md (spec + architecture + plan in one file), AGENTS.md. |
| **Full** | 2 days to ~2 weeks | All stages. Documents: BRIEF, SPEC, ARCHITECTURE, PLAN, AGENTS.md. |
| **Too big** | More than ~2 weeks | Not a track. Cut it to the smallest usable version, build that, then start again from Stage 0. |

**On Small, "ARCHITECTURE" and "PLAN" always mean the matching sections inside SPEC.md.** Never create them as separate files. If the stack is too big to fit readably in one file, the project belongs on Full.

The size estimate picks the track, not the owner's preference that day. When the estimate falls between two bands, take the higher one: too much ceremony costs boredom, too little costs a rebuild. Every track gets the repo and commits, because code that only exists in a session's container is lost.

### Shapes

The stages are the same for every shape. Only the prototype and the skeleton differ. **Every shape's prototype lives in `prototype/`.**

| Shape | Prototype (Stage 2): what the owner sees first | Walking skeleton (Stage 5): touches something real |
|---|---|---|
| Web app / SaaS | Clickable HTML of the core path, fake data | One route → one real data read → the core screen, live on the host |
| Static site / landing page | The real pages in HTML, near-final copy | One page built from one real content file, live on the host |
| CLI / script | `prototype/session.md`: a written terminal session with the core command, its output, and one error with a non-zero exit | One command reads real input, prints real output, exits non-zero on failure |
| Game / interactive | A playable greybox of the core loop, or storyboard frames in HTML if it cannot be played yet | A window opens, one real asset renders, one input changes the screen |
| Data pipeline / automation | A sample input next to the expected output, plus a mock run log with one failure | One real record moves from the real source to the real sink; a failure is visible |
| Something else | Agree on it in Stage 0: the cheapest thing the owner can *look at* that shows the core action | The thinnest thing that exercises the real wiring, with no features |

**The skeleton rule for every shape:** if it does not touch something real (a real file, request, asset or record), it is not a skeleton, it is a screenshot. A constant, a config value, a stub or a placeholder does not count. Screenshots are welcome in Stage 2, and not in Stage 5.

---

## Stage 0: Intake (10–15 minutes)

Collect five answers, one question at a time, offering options where the owner is unsure:

1. **The idea**, in 2–3 sentences, and **who it is for**.
2. **What it is NOT.** Name the non-goals; an unbounded scope never finishes.
3. **Size by hand.** This picks the track. More than ~2 weeks means helping the owner cut it now.
4. **Shape.** If it is "something else", agree on its prototype and skeleton lines.
5. **A one-word project name.** It becomes the folder name.

The hard questions (done-command, deploy target, stack) are deliberately **not** asked here. They are much easier to answer once the owner has seen the prototype, so they belong in Stage 3.

**Gate:** five answers, a track, a shape, a name.

## Repo setup (every track, straight after intake)

Do this yourself, in the session that will do the work. The point is to prove what *this session* can reach; the owner doing it in their own terminal proves nothing.

1. **Get into the project folder.**
   - If the session is already in a folder with the project's name, or in an empty folder (or one holding only this idea's files), ask whether to use it as the project folder. Do not create another folder inside it: a repo one level too deep passes every check and is not where the owner thinks it is.
   - If the session is in a parent folder (one holding other projects), create `<name>/` and move into it.
   - If your tool cannot change folders, create `<name>/` and run every command against it explicitly (`git -C <name>`, absolute paths), or ask the owner to reopen the session there. Never run `git init` in the parent folder.
2. **Initialise:**
   - `git init`.
   - `.gitignore`: make sure it contains `node_modules/`, `.env`, `.env.*`, `!.env.example`, `dist/` and `.DS_Store`. If one already exists, append only the lines it lacks and never remove any.
   - Write BRIEF.md (Template A) with Intake ticked.
   - Write a minimal AGENTS.md (Template E: header and "Every session"). If the tool you run in reads a differently named instruction file, add that pointer file now (see Template E).
   - If you are following this method from a file (`BUILD-MACHINE.md`) instead of an installed skill, copy that file into the project folder.
   - Commit: `chore: repo init + brief`.
3. **Verify, and show the owner both outputs:**
   - `git rev-parse --show-toplevel` must print the project folder itself. Ask the owner to confirm it is a folder they can open on their own machine.
   - `git log --oneline --stat` must show the commit, including .gitignore and BRIEF.md.

   If either is wrong, fix it. When both are right, tick Repo in Progress and amend the commit. This proves that the session can write into a repo, and that it is the right repo.

Commands are shown in POSIX shell. Use your shell's equivalent where needed.

A remote can wait until the first deploy, unless this is a cloud session (see "where are we?", step 1).

**Gate:** the session made the commit itself; `rev-parse` is the project folder; the owner confirmed it is on their disk (cloud session: pushed to a remote the owner controls, and the owner saw the commit there).

**Sketch stops following the stages here:**
- Build directly, and show something visible within ~15 minutes.
- Iterate with the owner.
- Wire one command that can fail (build, lint or a test), and run it.
- Commit, and deploy if anyone besides the owner will see it.
- Tick Progress, commit `chore: sketch green`, and tag `green/sketch`.

The rest of this document is for Small and Full.

---

## Stage 1: Screens interview (30–60 minutes)

Learn just enough to draw the prototype. No databases, auth or stack yet.

Ask, one at a time:
- **Primary user:** one concrete person, their situation, what they want.
- **Core action:** the single thing this product exists to let them do.
- **The path:** the 3–7 screens or moments they pass through to do it, in order.
- **For each screen:** what is on it, and what the user does there.
- **Awkward states:** empty (first use), error, lots of data.
- **The look:** reference sites they like, brand colours or assets, mood. If the owner has a design system or a personal style guide (a style skill, a brand file, reference sites), use it and say so. If not, ask: which two or three sites feel right, light or dark, calm or bold. Record the answer as the `Look:` line under **Screens** in BRIEF.md, so later sessions and the phase review use it too.
- **What already exists:** prior attempts, donor repos, brand assets, domains, accounts they hold. Reuse beats rebuild.

When you can describe the whole path, write it into BRIEF.md under **Screens** as a numbered click path, and read it back to the owner.

**Gate:** the owner confirms the click path. Tick Progress, commit `docs: screens`, and tag `green/screens`.

## Stage 2: Prototype (same day)

Build something the owner can click, so they judge the idea with their eyes instead of their imagination. This stage keeps the owner motivated, so make it look good.

**For web shapes** (other shapes: their row in the Shapes table):
- `prototype/index.html` (plus more pages if needed). Self-contained, no build step, no backend; it opens with a double-click.
- **Realistic fake data:** believable names, amounts and dates, and enough rows to feel real. Include the awkward states from Stage 1.
- **The whole core path is clickable** from start to finish. Buttons off the path may be dead, but mark them subtly (e.g. "not in prototype").
- **The owner's look**, from Stage 1. A generic-looking prototype gets judged as generic.
- **Check it yourself before showing it.** If you can render pages (a headless browser or a screenshot tool), check the core screens at phone (~390px), tablet (~768px) and desktop (~1280px) width, and fix what breaks. If you cannot render, say so.

**Show it.** Give the owner the path to open, or a preview link if your tool can publish one. Ask them to click through the core path, then ask what is wrong, what is missing and what surprised them.

**Iterate in rounds**, and commit each one: `proto: round N`. If the core path still changes fundamentally after three rounds, stop drawing: the idea is not settled. Untick "1 Screens", commit, and go back to Stage 1 for the part that keeps moving.

**The prototype is a drawing, not the product.** It shows how the product must look and feel. Its code is throwaway: do not grow it into the app. Stage 5 rebuilds in the real stack, reusing markup and styles where that helps.

**Gate:** the owner says, in their own words, that this is it. Record what clicking settled under **Prototype decisions** in BRIEF.md. Tick Progress, commit `proto: approved`, and tag `green/prototype`.

## Stage 3: Spec (the deep interview, walking the prototype)

Now ask the expensive questions, screen by screen. Each answer becomes concrete because the owner can see what it affects.

**For every piece of information on every screen:**
- **Where does it come from, and where is it stored?** This becomes the data model.
- **Who may see it, and who may change it?** This becomes auth and roles. Include the people behind the scenes, such as an admin or operator.
- **What happens when it is missing, wrong or slow?** These become the error states.
- **Does it depend on an outside service** (payments, email, maps, storage, forms, AI)? Each one later gets a build-time guard or an output check. Each claim about one (pricing, free tier, commercial-use terms, region) is dated: "as researched YYYY-MM-DD; re-check, don't trust."

**Then the decisions Stage 0 left open:**
- **Stack:** 2–3 options, the trade-off of each, and your recommendation for *this* project (not whatever is popular). Wait for approval.
- **Environment:** the owner's OS, runtime, package manager and versions. These get pinned.
- **Deploy target:** a host, a store, a registry, or "local only" and why. Hosting terms can rule out a stack, so check them now.
- **Done as a command:** which command or click path proves v1 is finished. Offer options.

When you could write the complete file tree, say so. That ends the interview.

**Write the documents** for your track (Full: SPEC, ARCHITECTURE, PLAN, AGENTS.md; Small: SPEC and AGENTS.md), from the templates. Do them one at a time. Read each back to the owner, and **commit each as soon as it is approved** (`docs: spec draft`): an interview's worth of decisions is the most expensive thing the repo will hold.

**Every prototype screen and action maps to at least one capability ID.** Reference screens by their number in the click path. SPEC says what must happen; the prototype shows how it should look.

**Clarify pass.** List every place the documents are underspecified, ambiguous, or assume something the owner did not say. Ask about each, one at a time, then update the documents.

**Gate:**
- The file tree is complete.
- There is a typed data model, if the shape has data.
- Every capability has an ID and an EARS criterion.
- Every screen maps to a capability.
- The stack is approved and pinned, the environment is pinned, and the deploy target and done-command are written down.
- Every open question names an owner.
- The clarify pass is done.

Tick Progress, commit `docs: spec pack`, and tag `green/spec-draft`.

## Stage 4: Cross-check (fresh context, before any code)

The context that wrote the documents cannot see its own assumptions: it re-reads its own reasoning as fact. So a reader that did not write them does the check.

- **With subagents:** give one only the repo path and Template F. It returns the report to you, and you present it to the owner.
- **Without subagents:** stop and ask the owner for a fresh session. That session finds "4 Cross-check" unticked and runs Template F itself.

The checker changes nothing. The owner decides on the conflicts. Then the main session (or the fresh session, if there were no subagents) applies the approved fixes. If a blocking conflict was fixed, the check runs once more in a fresh context (a new subagent, or stop and ask for a fresh session), because a fix can introduce a new conflict.

**Gate:** zero unresolved conflicts, found by a context that did not write the documents. Tick Progress, commit `docs: cross-check green`, tag `green/spec`. **Stop**, and ask the owner for a fresh session for the skeleton.

## Stage 5: Walking skeleton (fresh session)

This stage runs in a **fresh session**. Read every document, then tell the owner the stack, the phase order and the next phase. If you cannot, the documents are not where they should be.

Propose your approach and wait for approval. Then build the **thinnest real slice for this shape** (see the Shapes table). Usually that is the prototype's core screen, in the real stack, showing one real piece of data.

Three things belong to the skeleton, not to later phases:
- **The gate command.** Typecheck, lint, test and build (or one `verify` script that chains them), wired and passing. Every later gate is fiction until a command exists that can fail.
- **The first deploy.** Commit, then deploy that commit to where the product will really run, with its environment variables set. Host surprises are cheapest at this size. A deploy that fails on a missing required variable is the guard working.
- **`.env.example`.** Secrets never enter the repo. Every required variable fails the build loudly when absent, via the framework's env schema or a check in the gate script.

**Show the owner the live result** next to the prototype screen it came from.

**Gate:** the gate command exits 0; the slice touches something real; the deployed commit works where it will run (or, if local-only, is built for its real target); the owner has seen it. Then make one bookkeeping commit: tick Progress, set Phase 0 to `done` and the next phase to `next` in the order table, and tag it `green/phase-0`. **Stop.** Phase 1 starts in a fresh session.

## Stage 6: Build loop (one phase per fresh session)

For each phase:

1. **Fresh session.** Read the documents and take the phase marked `next` in the order table, **only that phase**. Quality drops as a context fills; a clean session holding the spec and one phase writes better code than one that has run for hours.
2. **Propose the approach and wait for approval.**
3. **Build the slice.**
   - Never edit a file you have not read in this session.
   - Never leave placeholders like "…rest unchanged". If the owner must change a file by hand (a host dashboard, for example), give the whole content.
   - No new dependencies and no change to the pinned stack without asking.
   - No features beyond SPEC: flag the gap instead of filling it.
4. **Run the gate command** and show its output. Red means not done; do not argue around it.
5. **Check the phase's EARS criterion** for real.
6. **Commit, and deploy to preview if the product is hosted.**
7. **Phase review, by a context that did not write the code.** The session that built the phase re-reads its own reasoning as fact, just as in Stage 4. A green gate command proves the code runs, not that it matches the prototype or works on a phone.
   - **With subagents:** give one the repo path, the phase and Template G. It changes nothing and reports to you.
   - **Without subagents:** run Template G yourself, and label the report "self-review: no independent context". Do not ask the owner for an extra session just for this; one fresh session per phase is enough ceremony.
   - **Blocking findings:** fix the ones that stay inside SPEC; one that needs a change outside SPEC goes to the owner as a decision. Re-run the gate command, commit (`fix: phase N review`), and review once more. If the second review still finds blocking problems, stop and show the owner both reports; this counts as a failed attempt (see "a phase that fails twice" below).
   - **Minor findings and judgment calls** (taste, scope) go to the owner with the result. Do not fix them unasked.
8. **Show the owner** the result (preview URL, screenshot or terminal transcript) next to the prototype screen it implements, with the review report. The owner never goes a whole phase without seeing something.
9. **When the owner approves:** make the bookkeeping commit (this phase `done`, the next one `next` in the order table) and tag it `green/phase-N`. A stale order table sends the next session to redo finished work, with no way to notice. If the owner does not approve, fix it, re-run the gate command, and show it again.
10. **Stop.** Report what changed and what is untested. The next phase starts in a new session.

A phase that fails twice is too big: split phase N into Na and Nb (two rows in the order table, tags `green/phase-Na` and `green/phase-Nb`) and do the halves. Phase numbers are labels. Never renumber them, because commits and tags cite them.

**Ship** is the last phase:
- The product is reachable where it is meant to be.
- Env vars are set everywhere it runs.
- Every external integration has been tested live once (one real submission, login or payment).
- "Blocked on the owner" is empty, and no open question owned by the owner remains.

For Ship, the bookkeeping commit also ticks "6 Build" in Progress, and the tag is `green/ship` (not a phase number).

## Stage 7: Recovery (when a session goes sideways)

Do not fix it by chatting more in the same session: its context is polluted. Go back to the last green tag:

```bash
git tag -l 'green/*' --sort=-creatordate | head -1   # the last approved state
git log --oneline <that tag>..HEAD                   # commits that a reset would DISCARD
git status                                           # uncommitted changes the session made
git clean -nd                                        # PREVIEW untracked files it created
```

Show the owner all of this and let them choose the target. Usually it is the last green tag, but it can be a later commit they approved (for example a finished `docs: spec draft`). Wait for a yes. Then:

```bash
git reset --hard <chosen target>     # tracked files back to the chosen state
git clean -fd                        # remove the previewed files (never -x: that deletes .env too)
```

Start a fresh session, re-read the documents, and retry with an instruction that names what went wrong. If it fails twice, split the phase.

## Retro (after Ship, or when abandoning)

Ask the owner five quick questions and append the answers to `RETRO.md`:

1. How long from idea to the first click on the prototype?
2. Where did you get stuck or lose motivation?
3. Which gate caught a real problem, and which felt like pure ceremony?
4. What did the prototype get wrong that only showed up later?
5. What would you change about this method?

Tick Retro, commit `docs: retro`. This is how the method improves: from real projects, not from rewriting it on a good evening.

---

## Gates at a glance

| Stage | Gate |
|---|---|
| 0 Intake | Five answers · track · shape · name |
| Repo | Session committed itself · `rev-parse` = project folder · on the owner's disk (or pushed to their remote) |
| Sketch | Gate command exits 0 · does what was asked · committed · deployed if others see it |
| 1 Screens | Owner confirmed the click path |
| 2 Prototype | Core path clickable · checked at 3 widths if web (or said why not) · owner says "this is it" |
| 3 Spec | File tree · typed model (if data) · ID + EARS per capability · every screen → capability · stack, environment, deploy target, done-command fixed · open questions owned · clarify done |
| 4 Cross-check | Zero unresolved conflicts, from a context that did not write the docs |
| 5 Skeleton | Gate green · touches something real · deployed and working · owner saw it |
| 6 Each phase | Gate green · EARS holds · reviewed with Template G (independent if subagents exist), no blocking findings left · owner saw it with the report and approved · order table updated · tagged |
| Ship | Reachable · env vars set · integrations tested live · nothing blocked on the owner |

## Anti-patterns not covered above

- **The owner as courier.** Documents copied between windows end up in a chat log, where nothing can read, check or restore them. Work where the files are.
- **"Comprehensive" as a requirement.** It invents features. List the features instead.
- **Trusting outside services from memory.** A form that posts nowhere passes every local gate and silently drops every enquiry. Date every claim, and guard every dependency.

---

# Templates

You fill these in; the owner never writes them by hand. Delete sections that do not apply to the shape instead of leaving them empty.

## A · BRIEF.md (every track: the project's memory)

```markdown
# BRIEF: [Project name]

## Intake
- Idea: [2–3 sentences: what, for whom]
- Not building: [non-goals]
- Size by hand → track: [few hours = Sketch / ≤2 days = Small / ≤2 weeks = Full]
- Shape: [web app / static site / CLI / game / pipeline / other: prototype = …, skeleton = …]
- Name: [one word = folder name]

## Screens (Stage 1: the core path as a numbered click path)
Look: [style guide or skill by name, or 2–3 reference sites · light/dark · calm/bold]
1. [Screen]: [what is on it] → [what the user does]

## Prototype decisions (Stage 2: what clicking settled)
- …

## Progress (tick and commit as each gate passes)
- [x] 0 Intake
- [ ] Repo (ticked after the two checks pass)
- [ ] 1 Screens
- [ ] 2 Prototype
- [ ] 3 Spec
- [ ] 4 Cross-check
- [ ] 5 Skeleton
- [ ] 6 Build (see the order table)
- [ ] Ship
- [ ] Retro
```

For a Sketch, Progress is only: Intake, Repo, "Built: gate green, committed, deployed if others see it".

## B · SPEC.md

```markdown
# SPEC: [Project name]

## Objective
[One sentence: who uses this and what outcome they get.]

## Primary user
[One concrete person: their context and goal.]

## Core action
[The single thing this product exists to let them do.]

## Capabilities (v1): ID, EARS criterion, prototype screens covered
- C1 [name] (screens 1–2): WHEN [trigger], the system SHALL [response].
- C2 [name] (screen 3): The system SHALL [behaviour].
- C3 [name] (screen 3, error state): IF [condition], THEN the system SHALL [response].

## Prototype
`prototype/`, approved [date]: the visual reference for every screen above. Where SPEC and prototype disagree, SPEC wins and the conflict is flagged.

## Explicitly NOT in scope
- [What people will assume is included but is not]

## Done when
[Command or click path that proves all v1 capabilities pass.]

## Open questions (each names its owner)
- [Owner: owner] [account to create, asset to supply, decision to make]
- [Owner: agent] [research or drafting still to do]
```

EARS: every "done when" fits one of these patterns, or it is still too vague to build.

| Pattern | Form |
|---|---|
| Ubiquitous | The system SHALL [do X]. |
| Event | WHEN [trigger], the system SHALL [response]. |
| State | WHILE [state], the system SHALL [behaviour]. |
| Unwanted | IF [condition], THEN the system SHALL [response]. |

## C · ARCHITECTURE.md (Full; on Small these are sections of SPEC.md)

```markdown
# ARCHITECTURE: [Project name]

## Shape
[shape + its skeleton line]

## Stack (pinned: do not substitute without asking). Only the layers this project actually has.
| Layer | Choice | Version |
|---|---|---|
| Runtime | | |
| Language | | |
| [frontend / backend / database / ORM / auth / storage / engine / source / sink …] | | |
| Hosting / deploy | [host + trigger, or "local only" and why] | |
| Test runner | | |

## Environment
OS · runtime manager · package manager + versions

## File tree (complete)

## Data model (if the shape has data)
### [Entity]
| Field | Type | Constraints |
|---|---|---|
Relations: …

## Interfaces (API routes / CLI flags / events / pipeline stages, whichever exist)
METHOD /path · request · response · errors

## Deployment
Host · ships via … · runtime pinned by …
| Env var | Required | Guarded by |
|---|---|---|
Dashboard settings outside the repo that change what users get: …
Every claim about a third-party service carries "as researched YYYY-MM-DD; re-check, don't trust."

## Key decisions
- Chose X over Y because Z. Cost: [what it makes harder].
```

## D · PLAN.md (Full; on Small this is a section of SPEC.md)

```markdown
# PLAN: [Project name]

## Order: this table is the instruction
| Order | Phase | Status |
|---|---|---|
| 1 | Phase 0: Skeleton | next |
| 2 | Phase 1: [name] | todo |
(Numbers are labels: reorder freely, never renumber.)

## Blocked on the owner
- [account / asset / content / legal read]: blocks Phase [n]

## Phase 0: Skeleton
Thinnest real slice for this shape: [row from Shapes]. A constant, config value, stub or placeholder does not count; it must touch something real.
Includes the gate command, .env.example and the first deploy.
- Done when: gate command exits 0 · slice touches something real · deployed and working where it will run
- Tag: green/phase-0

## Phase 1: [name]
- Delivers: C1 (screens 1–2)
- Done when: [EARS criterion]. Verified by [command or click path]
- Owner sees: [preview URL / screenshot / transcript]
- Tag: green/phase-1

## Phase N+1: Ship
- Done when: reachable where it is meant to be · env vars set · every external integration tested live once · nothing blocked on the owner
- Tag: green/ship

## Deferred (v2)
- …
```

## E · AGENTS.md (the rules every session re-reads, in any AI tool)

Create the header and "Every session" sections at repo setup. Complete the rest in Stage 3.

```markdown
# AGENTS.md: [Project name]

This project follows the Build Machine method (the build-machine skill, or BUILD-MACHINE.md in this repo if the skill is not installed). Start every session by reading BRIEF.md (Progress) and following the method from where Progress says we are.

## Every session
- Read BRIEF.md, then the spec documents that exist (SPEC.md; on Full also ARCHITECTURE.md and PLAN.md).
- Match the pinned runtime before any install; a wrong runtime writes a wrong lockfile.
- Follow Progress in BRIEF.md. From Stage 5 on, work only on the phase marked `next` in the order table.
- If this session's disk is temporary (cloud or sandbox), push after every commit.
- Propose your approach and wait for approval before writing files.
- Never edit a file you have not read this session. Never leave "…rest unchanged" placeholders.
- Never write code while a cross-check conflict is unresolved.

## Constraints
- No new dependencies and no change to the pinned stack without asking.
- No features beyond SPEC.md: flag gaps instead of filling them.
- `prototype/` is the visual reference: do not import from it or extend it.

## Verification
Before claiming a phase done, run and show: [gate command, e.g. npm run verify]. Then confirm the phase's EARS criterion. Red = not done.
Then have the phase reviewed with Template G of the build-machine method by a context that did not write it (a subagent), or run it yourself and label it "self-review". Fix blocking findings, re-run the gate, and show the owner the report.

## Stop
After each phase: show the owner the result, report what changed and what is untested, and after approval update the order table and tag green/phase-N. Then stop.
```

If the tool you are running in reads a differently named instruction file instead of AGENTS.md, create that file with one line pointing to AGENTS.md (for Claude Code: a `CLAUDE.md` containing `@AGENTS.md`).

## F · Cross-check prompt (for the fresh context)

```text
Do not write code and do not edit files. Cross-check this repo's spec pack
(BRIEF.md, SPEC.md, and on Full ARCHITECTURE.md and PLAN.md, plus prototype/)
against itself. Report conflicts only:
- Every capability maps to at least one plan phase (flag orphans).
- Every plan phase delivers a real capability (flag inventions).
- Every prototype screen and action maps to a capability, and every
  capability with a UI has a screen (flag gaps both ways).
- The data model and interfaces cover what the capabilities need, including
  who creates each piece of data (flag gaps).
- Every external service has a named build-time guard or output check, and
  every claim about it is dated (flag bare trust).
- The skeleton phase touches something real (not a constant, config or
  stub), includes the gate command and a first deploy.
- Nothing in scope is missing; nothing out of scope has crept in.
Report format:
1. One-line verdict: green, or "N blocking, M minor".
2. Blocking conflicts first (they change the data model, the scope or a
   phase), each in at most 3 lines: what, where (file + section), proposed fix.
3. Minor gaps, one line each.
4. The decisions the owner must make. If you are talking to the owner
   directly, ask the first one only.
```

## G · Phase review prompt (Stage 6, for a context that did not write the code)

```text
Do not edit files. Review one finished build phase of this repo.
Read BRIEF.md, SPEC.md (on Full also ARCHITECTURE.md and PLAN.md),
AGENTS.md, and the prototype screens this phase implements.
Phase: [Phase N: name] · capabilities [C…] · screens [n…]
Changes: git diff [last green tag]..HEAD
Run it: [preview URL, or the local start command]
Check:
- Behaviour: exercise the phase's EARS criterion for real (click path
  or command), including the empty, error and lots-of-data states the
  spec names for these screens.
- Widths (web shapes): render each screen of this phase at ~390px,
  ~768px and ~1280px. Flag overflow, overlap, cut-off text, unreadable
  contrast, tap targets too small to use, and layouts that break. If
  you cannot render pages, say so; do not guess.
- Looks: compare each screen with its prototype screen, and with the
  style named on the Look line in BRIEF.md (read that style guide or
  skill if it is available to you). Flag visible drift from them, not
  your own taste.
- Code: bugs, unhandled errors, duplication, unused files, secrets or
  real env values in the repo, anything that breaks a rule in AGENTS.md.
- Scope: anything built beyond SPEC (flag inventions), anything this
  phase promised but did not deliver (flag gaps).
Report format:
1. One-line verdict: green, or "N blocking, M minor".
2. Blocking first: anything that breaks the EARS criterion, a width,
   the prototype's core path, or a rule in AGENTS.md. Each in at most
   3 lines: what, where (file + line, or screen + width), proposed fix.
3. Minor findings, one line each.
4. Judgment calls for the owner (taste, scope), as questions.
```
