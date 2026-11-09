import sys, json, os, argparse
from faster_whisper import WhisperModel
ap = argparse.ArgumentParser(description="Timed transcript: .srt + .words.json + .txt")
ap.add_argument("audio"); ap.add_argument("--model", default=os.environ.get("AI_WHISPER_MODEL", "small"))
ap.add_argument("--lang", default=None); ap.add_argument("--out", default=None)
a = ap.parse_args()
base = a.out or os.path.splitext(a.audio)[0]
m = WhisperModel(a.model, device="cpu", compute_type="int8", download_root=os.path.expanduser("~/ai-tools/models/whisper"))
segs, info = m.transcribe(a.audio, language=a.lang, word_timestamps=True, vad_filter=True)
def ts(t):
    h, r = divmod(t, 3600); mi, s = divmod(r, 60); return f"{int(h):02}:{int(mi):02}:{int(s):02},{int((s%1)*1000):03}"
srt, words, txt = [], [], []
for i, s in enumerate(segs, 1):
    srt.append(f"{i}\n{ts(s.start)} --> {ts(s.end)}\n{s.text.strip()}\n"); txt.append(s.text.strip())
    words += [{"word": w.word.strip(), "start": round(w.start, 2), "end": round(w.end, 2)} for w in (s.words or [])]
open(base + ".srt", "w").write("\n".join(srt)); open(base + ".txt", "w").write("\n".join(txt) + "\n")
json.dump(words, open(base + ".words.json", "w"), indent=1)
print(f"lang={info.language} -> {base}.srt / .txt / .words.json ({len(words)} words)")
