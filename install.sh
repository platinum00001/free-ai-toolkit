#!/usr/bin/env bash
# Rebuild the Free AI Toolkit on any Linux box (shared box, Hostinger VPS, or a cloud VM).
# Needs: curl, git, ffmpeg, python3. Installs uv if missing. CPU-only; ~15 GB disk with models.
set -euo pipefail
ROOT="${AI_TOOLS:-$HOME/ai-tools}"; mkdir -p "$ROOT"/{venvs,models,logs} "$HOME/.local/bin"
command -v uv >/dev/null || curl -LsSf https://astral.sh/uv/install.sh | sh
export PATH="$HOME/.local/bin:$PATH" UV_LINK_MODE=copy
CPU_TORCH="--index-url https://download.pytorch.org/whl/cpu"
cd "$ROOT"
[ -d venvs/rap ]    || { uv venv -q --python 3.11 venvs/rap && uv pip install -q --python venvs/rap/bin/python torch torchaudio $CPU_TORCH && uv pip install -q --python venvs/rap/bin/python "audio-separator[cpu]" faster-whisper demucs; }
[ -d venvs/midi ]   || { uv venv -q --python 3.11 venvs/midi && uv pip install -q --python venvs/midi/bin/python "basic-pitch[onnx]" "numpy<2" "ml_dtypes==0.2.0"; }
[ -d venvs/kokoro ] || { uv venv -q --python 3.11 venvs/kokoro && uv pip install -q --python venvs/kokoro/bin/python torch $CPU_TORCH && uv pip install -q --python venvs/kokoro/bin/python kokoro soundfile; }
[ -d venvs/scrape ] || { uv venv -q --python 3.11 venvs/scrape && uv pip install -q --python venvs/scrape/bin/python "scrapling[fetchers]"; }
[ -x ollama/bin/ollama ] || { mkdir -p ollama && curl -L https://ollama.com/download/ollama-linux-amd64.tar.zst | tar --zstd -x -C ollama; }
chmod +x bin/ai-*
for f in bin/ai-*; do case "$f" in *.py) ;; *) ln -sf "$ROOT/$f" "$HOME/.local/bin/$(basename "$f")";; esac; done
echo "Installed. Run: ai-tools   (lists every command)"
echo "Optional 3D coder model (2.7 GB): ai-llm add 3dcoder ccore/Qwen3.5-4B-3D-Coder Qwen3.5-4B-3D-Coder-Q4_K_M.gguf"
