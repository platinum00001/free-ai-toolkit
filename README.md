# Free AI Toolkit (shared box)

Free, open-source AI tools installed permanently on the shared box at `~/ai-tools`, callable by name from any bot's shell (`~/.local/bin` is on PATH). Run `ai-tools` to list them. Everything runs on CPU, under `nice`, so it won't starve other bots' work; on a busy box expect minutes, not seconds.

Repo (scripts, installer, GPU notebooks): https://github.com/platinum00001/free-ai-toolkit . Rebuild anywhere (e.g. a Hostinger VPS) with `git clone https://github.com/platinum00001/free-ai-toolkit ~/ai-tools && ~/ai-tools/install.sh`.

## Commands

| Command | What it does | Example |
|---|---|---|
| `ai-vocals SONG [OUTDIR]` | Two-pass split: vocals vs instrumental (BS-Roformer), then lead vocal vs backing vocals (UVR MDX karaoke). Outputs `NAME_lead_vocal.wav`, `NAME_backing_vocals.wav`, `NAME_instrumental.wav` | `ai-vocals song.mp3 out/` |
| `ai-stems SONG [OUTDIR] [--six]` | Demucs stems: drums, bass, vocals, other (`--six` adds guitar, piano) | `ai-stems song.mp3 stems --six` |
| `ai-midi AUDIO [OUTDIR]` | Spotify basic-pitch: audio to `.mid` (melody, chords, bassline) for re-producing a beat | `ai-midi instrumental.wav midi/` |
| `ai-lyrics AUDIO [--model small] [--lang en] [--out BASE]` | faster-whisper with word timestamps: `BASE.srt`, `BASE.txt`, `BASE.words.json` (works on video too) | `ai-lyrics lead_vocal.wav --model medium` |
| `ai-tts "TEXT"\|@file.txt [OUT.wav] [--voice V] [--speed 1.0]` | Kokoro-82M natural TTS. Voices: `af_heart`, `af_bella`, `am_michael`, `am_adam`, `bf_emma`, `bm_george` and more (list: https://huggingface.co/hexgrad/Kokoro-82M/blob/main/VOICES.md) | `ai-tts @line.txt mara.wav --voice bf_emma` |
| `ai-captions VIDEO [OUT] [--srt FILE] [--model small]` | Auto-transcribes and burns bold, outlined captions | `ai-captions trailer.mp4` |
| `ai-vertical VIDEO [OUT] [--crop] [--start T --dur S]` | 1080x1920 9:16 clip for Reels/TikTok/Shorts (blurred-background pad, or `--crop`) | `ai-vertical trailer.mp4 short.mp4 --start 00:00:10 --dur 30` |
| `ai-scrape URL [CSS] [--stealth] [--json]` | Scrapling fetch: prints text + link per element (default `a`). `--stealth` uses a headless stealth browser for JS/anti-bot pages | `ai-scrape https://example.org/resources "li a" --json` |
| `ai-llm start\|stop\|status\|list` | Ollama local LLM server, on demand only (niced, 1 model, unloads after 2 min) | `ai-llm status` |
| `ai-llm ask MODEL "PROMPT"\|@file` | Starts Ollama if needed, answers, stops it again | `ai-llm ask 3dcoder "three.js snow particles"` |
| `ai-llm add NAME HF_REPO FILE.gguf` | Downloads a GGUF from Hugging Face with curl and registers it (needed because `ollama pull hf.co/...` is blocked on this box's network) | `ai-llm add qwen-tiny unsloth/Qwen3.5-0.8B-GGUF Qwen3.5-0.8B-Q4_K_M.gguf` |
| `ai-3d "SCENE" [OUT.html]` | Qwen3.5-4B-3D-Coder writes a single-file Three.js scene (slow on CPU when the box is busy) | `ai-3d "armored convoy on an ice ridge, falling snow" convoy.html` |

Installed models in Ollama: `qwen-small` (Qwen3.5-2B Q4_K_M, 1.3 GB, general helper) and `3dcoder` (Qwen3.5-4B-3D-Coder Q4_K_M, 2.7 GB). Whisper and separation models download on first use into `~/ai-tools/models/`.

## Recipes
- Rap remix: `ai-vocals song.mp3 out/` then `ai-midi out/song_instrumental.wav midi/` then `ai-lyrics out/song_lead_vocal.wav`, then remix with ffmpeg (e.g. `ffmpeg -i out/song_instrumental.wav -i new_vocal.wav -filter_complex amix=inputs=2 remix.wav`).
- Cutscene voices: one `ai-tts @line.txt line01.wav --voice ...` per line, then mix with ffmpeg.
- Social short: `ai-vertical trailer.mp4 v.mp4 --dur 30 && ai-captions v.mp4 short.mp4`.
- Nightly resource / deals radar: `ai-scrape URL "css" --json > today.json`, diff against yesterday, summarize with `ai-llm ask`.

## Layout
- `bin/` wrapper scripts (symlinked into `~/.local/bin`), `venvs/` isolated uv environments (rap: audio-separator, demucs, faster-whisper; midi: basic-pitch; kokoro; scrape: scrapling), `ollama/` Ollama 0.40.15 binary, `models/` downloaded weights, `notebooks/` GPU notebooks, `GPU_TOOLS.md` free GPU options.

## GPU-only tools
ACE-Step 1.5 (songs), Wan2.2 / LTX-2 (video), ComfyUI, Idol / TRELLIS.2 / Hunyuan3D (3D), OmniVoice (voice cloning): see `GPU_TOOLS.md` for Colab/Kaggle notebooks and free Hugging Face Spaces.

## House rules for bots
- Always run heavy jobs through these wrappers (they `nice` themselves). Don't leave Ollama running: use `ai-llm ask`, or `ai-llm stop` after `ai-llm chat`.
- Write outputs to your own work folder, not inside `~/ai-tools`.
- Licenses: all tools are open source; LTX-2 and Hunyuan3D weights have community licenses (fine for small creators, read them before commercial use at scale).
