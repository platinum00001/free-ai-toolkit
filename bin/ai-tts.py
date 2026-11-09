import sys, argparse, numpy as np, soundfile as sf, warnings
warnings.filterwarnings("ignore")
ap = argparse.ArgumentParser(description="Kokoro TTS")
ap.add_argument("text", help="text, or @file.txt"); ap.add_argument("out", nargs="?", default="tts.wav")
ap.add_argument("--voice", default="af_heart"); ap.add_argument("--speed", type=float, default=1.0)
ap.add_argument("--lang", default=None, help="a=US b=UK e=es f=fr h=hi i=it j=ja p=pt z=zh (default from voice)")
a = ap.parse_args()
text = open(a.text[1:]).read() if a.text.startswith("@") else a.text
from kokoro import KPipeline
p = KPipeline(lang_code=a.lang or a.voice[0], repo_id="hexgrad/Kokoro-82M")
audio = np.concatenate([au for _, _, au in p(text, voice=a.voice, speed=a.speed)])
sf.write(a.out, audio, 24000); print(f"{a.out} ({len(audio)/24000:.1f}s, voice {a.voice})")
