import subprocess, sys, json, os
D = os.path.dirname(os.path.abspath(__file__))
os.chdir(D)
# (file, in_point, duration, timeline_start, sfx_gain)
SEG = json.load(open('segments.json'))
XF = 0.5  # S6 -> S7 dissolve
inputs = []
fc = []
for i, (f, a, d, st, g) in enumerate(SEG):
    inputs += ['-i', f]
    fc.append(f"[{i}:v]trim=start={a}:duration={d},setpts=PTS-STARTPTS,fps=25,scale=1920:1080:flags=lanczos,setsar=1,format=yuv420p,settb=AVTB[v{i}]")
    fc.append(f"[{i}:a]atrim=start={a}:duration={d},asetpts=PTS-STARTPTS,aformat=sample_rates=48000:channel_layouts=stereo,volume={g},afade=t=in:d=0.04,afade=t=out:st={d-0.06}:d=0.06,adelay={int(st*1000)}|{int(st*1000)}[a{i}]")
n = len(SEG)
# hard cuts S1..S6, dissolve S6->S7
fc.append("".join(f"[v{i}]" for i in range(n - 1)) + f"concat=n={n-1}:v=1:a=0,settb=AVTB[vmain]")
off = SEG[-1][3]  # S7 timeline start == xfade offset
fc.append(f"[vmain][v{n-1}]xfade=transition=fade:duration={XF}:offset={off}[vcut]")
# white flash on wave impact cut (S4->S5)
flash_t = SEG[4][3]
fc.append(f"color=c=white:s=1920x1080:r=25:d=0.24,format=rgba,fade=t=in:st=0:d=0.06:alpha=1,fade=t=out:st=0.08:d=0.16:alpha=1,setpts=PTS+{flash_t-0.08}/TB[fl]")
fc.append("[vcut][fl]overlay=eof_action=pass[vf]")
# grade + grain + vignette
fc.append("[vf]eq=contrast=1.03:saturation=0.97,vignette=angle=PI/6,noise=alls=4:allf=t,format=yuv420p[vg]")
# captions
CAPS = [('cap_london.png', 3.85, 6.75), ('cap_road.png', 7.3, 9.75), ('cap_coast.png', 10.3, 13.3),
        ('cap_suede.png', 17.9, 20.4), ('end_tag.png', 21.0, 25.0), ('end_logo.png', 22.3, 25.0)]
last = 'vg'
base = n
for j, (png, s, e) in enumerate(CAPS):
    k = base + j
    dur = e - s
    inputs += ['-loop', '1', '-framerate', '25', '-t', f'{dur:.2f}', '-i', png]
    fo = f",fade=t=out:st={dur-0.35:.2f}:d=0.35:alpha=1" if e < 24.9 else ""
    fc.append(f"[{k}:v]format=rgba,fade=t=in:st=0:d=0.45:alpha=1{fo},setpts=PTS-STARTPTS+{s}/TB[c{j}]")
    fc.append(f"[{last}][c{j}]overlay=eof_action=pass:format=auto[o{j}]")
    last = f"o{j}"
fc.append(f"[{last}]fade=t=in:st=0:d=0.35,fade=t=out:st=24.45:d=0.55,trim=duration=25,format=yuv420p[vout]")
# music: A (0-17.6) + B (reuse 3.0-10.6 cello passage) from 17.4
m = base + len(CAPS)
inputs += ['-i', 'music.mp3']
fc.append(f"[{m}:a]asplit=2[ma][mb]")
fc.append("[ma]atrim=0:17.6,asetpts=PTS-STARTPTS,afade=t=out:st=17.1:d=0.5,aformat=sample_rates=48000:channel_layouts=stereo[mA]")
fc.append("[mb]atrim=3.0:10.6,asetpts=PTS-STARTPTS,afade=t=in:d=1.2,afade=t=out:st=5.6:d=2.0,aformat=sample_rates=48000:channel_layouts=stereo,adelay=17400|17400[mB]")
fc.append("[mA][mB]amix=inputs=2:normalize=0[mus]")
fc.append("".join(f"[a{i}]" for i in range(n)) + f"amix=inputs={n}:normalize=0,volume=0.55[sfx]")
fc.append("[mus][sfx]amix=inputs=2:normalize=0,atrim=0:25,afade=t=out:st=24.2:d=0.8,loudnorm=I=-14:TP=-1.0:LRA=11,aresample=48000[aout]")
out = sys.argv[1] if len(sys.argv) > 1 else 'MARINE_master.mp4'
cmd = ['ffmpeg', '-y', '-loglevel', 'error'] + inputs + ['-filter_complex', ';'.join(fc), '-map', '[vout]', '-map', '[aout]',
       '-c:v', 'libx264', '-preset', 'slow', '-crf', '16', '-profile:v', 'high', '-pix_fmt', 'yuv420p', '-movflags', '+faststart',
       '-c:a', 'aac', '-b:a', '256k', '-t', '25', out]
r = subprocess.run(cmd)
sys.exit(r.returncode)
