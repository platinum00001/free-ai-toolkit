# GPU-only tools: where they run for free

The shared box has no GPU, so these run in a free GPU notebook (Google Colab "T4 GPU", or Kaggle "GPU T4 x2" with Internet on) or on a free Hugging Face Space. Open a notebook straight from GitHub:
`https://colab.research.google.com/github/platinum00001/free-ai-toolkit/blob/main/notebooks/<file>.ipynb`
(Kaggle: New Notebook > File > Import Notebook > GitHub URL.) Both need James's own Google / Kaggle login; free tiers have usage limits.

| Tool | What for | Notebook | Free Space (no install) | License |
|---|---|---|---|---|
| ACE-Step 1.5 | Full songs with vocals (free Suno-style), LoRA on your own songs | notebooks/01_ace_step_music.ipynb | https://huggingface.co/spaces/ACE-Step/Ace-Step-v1.5 | MIT |
| Wan2.2 TI2V-5B | Image/text to video | notebooks/02_wan22_image_to_video.ipynb | https://huggingface.co/spaces/Wan-AI/Wan2.2-S2V (speech-to-video), https://huggingface.co/spaces/alexnasa/Wan2.2-Animate-ZEROGPU | Apache-2.0 |
| LTX-2 / LTX-2.3 | Image/text to video with audio | notebooks/03_comfyui_video_ltx.ipynb (ComfyUI templates) | https://huggingface.co/spaces/Lightricks/LTX-2-3 , https://huggingface.co/spaces/Lightricks/ltx-2-distilled | LTX-2 community license |
| ComfyUI | Node workflows for video, image, 3D | notebooks/03_comfyui_video_ltx.ipynb | n/a | GPL-3.0 |
| Idol | One image to 3D Gaussian splat (.ply) | notebooks/04_idol_image_to_3d.ipynb | https://huggingface.co/spaces/speridlabs/idol | Apache-2.0 |
| TRELLIS.2 | Image to textured GLB mesh (needs 24 GB: use the Space) | n/a | https://huggingface.co/spaces/microsoft/TRELLIS.2 | MIT |
| Hunyuan3D 2.1 | Image to 3D mesh | n/a | https://huggingface.co/spaces/tencent/Hunyuan3D-2.1 | Tencent community license |
| OmniVoice | Voice cloning, 600+ languages | Colab: https://colab.research.google.com/github/k2-fsa/OmniVoice/blob/master/docs/OmniVoice.ipynb | https://huggingface.co/spaces/k2-fsa/OmniVoice | Apache-2.0 |

Tip: bring results back to the box (Drive or download) and finish them with the CPU tools: `ai-captions`, `ai-vertical`, `ai-tts`, `ai-vocals`.
