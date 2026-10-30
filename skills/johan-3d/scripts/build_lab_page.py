import base64,glob,json,os
t=open('template.html').read()
glb=open('out/drone.opt.glb','rb').read()
fs=sorted(glob.glob('out/webpflat/*.webp'))
frames=['data:image/webp;base64,'+base64.b64encode(open(f,'rb').read()).decode() for f in fs]
poster='data:image/webp;base64,'+base64.b64encode(open('out/poster.webp','rb').read()).decode()
t=(t.replace('__GLB__',base64.b64encode(glb).decode()).replace('__FRAMES__',json.dumps(frames))
    .replace('__POSTER__',poster).replace('__GLB_KB__',str(round(len(glb)/1024)))
    .replace('__FRAMES_KB__',str(round(sum(os.path.getsize(f) for f in fs)/1024))))
open('/mnt/user-data/outputs/drone-3d-lab.html','w').write(t)
print(round(os.path.getsize('/mnt/user-data/outputs/drone-3d-lab.html')/1e6,2),'MB', len(fs),'frames')
