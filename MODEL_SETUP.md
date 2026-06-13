# 🤖 AI Model Setup — Dubai-DIFC · Honest Privacy Guide

The tool stores everything on your laptop. The AI model you connect determines your privacy.

> **For client matters, UAE PDPL-sensitive work, or DIFC-DPL-sensitive work: use local-only mode (Option A).**

---

## 🎯 The honest privacy table

| Option | Where it runs | Who can see your queries | Cost (AED/month) | Best for |
|---|---|---|---|---|
| 🥇 **Ollama + Qwen3 (local)** | Your laptop | ONLY you | AED 0 forever | **Client matters · PDPL-sensitive · DIFC-DPL-sensitive work · cross-border-restricted data** |
| 🥈 **DeepSeek API** | DeepSeek servers (China) | DeepSeek (opt-out available) | AED 8-20 moderate use | NON-client work · templates · public-law research |
| 🥉 **Claude API** | Anthropic servers (USA) | Anthropic (no training per policy) | AED 80-300 | Heavy daily users |
| 🥉 **Gemini API** | Google servers (USA + globally) | Google | AED 25-100 | Long-PDF synthesis |

---

## 🥇 Option A — Ollama + Qwen3 (local · RECOMMENDED · DEFAULT)

### Why local is the right choice for Dubai practice

- Model runs ON YOUR LAPTOP. Queries never leave.
- No PDPL Article 22 cross-border transfer concern.
- No DIFC-DPL Articles 26-31 international transfer concern.
- Suitable for client matters, draft submissions to DIFC Courts or onshore courts, confidential commercial advice.
- Aligned with UAE AI Charter 2024 principles on data sovereignty.

### One-command install (v0.2 will ship — manual for now)

```bash
# v0.1 manual setup:
brew install ollama
ollama pull qwen3:14b
# Edit ~/.ailawfirm-dubai/config.json with ollama provider
```

### Manual install

**Mac:** `brew install ollama` (or download from https://ollama.com/download/Mac)
**Windows:** Download from https://ollama.com/download
**Linux:** `curl -fsSL https://ollama.com/install.sh | sh`

```
ollama pull qwen3:14b
```

Alternative models:
- `ollama pull qwen3:7b` — 4 GB · faster, slightly lower quality
- `ollama pull llama3.3:8b` — 5 GB · Meta's model
- `ollama pull mistral:7b` — 4 GB · European model

Edit `~/.ailawfirm-dubai/config.json`:

```json
{
  "ai_provider": "ollama",
  "ollama_model": "qwen3:14b",
  "ollama_host": "http://localhost:11434"
}
```

### Hardware reality check

- MacBook Air M1/M2 8GB: works with `qwen3:7b`
- MacBook Air M2/M3/M4 16GB+: smooth with `qwen3:14b`
- Windows laptop 16GB + dGPU: smooth with `qwen3:14b`
- Older Windows 4-8GB no GPU: `qwen3:7b` or smaller

---

## 🥈 Option B — DeepSeek API (cheap cloud · NOT for client work)

### MANDATORY privacy setup before any use

DeepSeek's default ToS permits use of API inputs for training. **You must opt out.**

1. Go to https://platform.deepseek.com → Settings → Privacy
2. Toggle OFF "Allow my API requests to be used for model training"

Even after opt-out, DeepSeek servers (in China) process queries in transit. Under UAE PDPL Article 22, China is not currently on the UAE Data Office adequate-jurisdiction list. **For client matter data, do NOT use DeepSeek even with opt-out.**

### Setup

```bash
# v0.1 manual:
# Add DEEPSEEK_API_KEY env var · update config.json with deepseek provider
```

---

## 🥉 Option C — Claude API (Anthropic)

Top-tier reasoning. Anthropic does not use API inputs for training (per public policy). But queries still cross into Anthropic's USA servers — Article 22 PDPL territory. Use only with explicit consideration of cross-border transfer obligations.

---

## 🥉 Option D — Gemini API (Google)

Best for long-PDF synthesis. Google's terms vary by tier (paid Workspace tier has better data-isolation than free tier). Read the specific tier's terms before use.

---

## ⚠️ Cloud-mode consent (v0.2 will enforce; document principle now)

Whenever you enable cloud mode, the principle is:

```
⚠️  CLOUD MODE WARNING

Your queries will leave your laptop and be processed on [VENDOR]'s servers.

DO NOT use cloud mode for:
  ❌ Confidential client matter data
  ❌ Personal data under UAE PDPL Article 22 (cross-border restricted)
  ❌ Personal data under DIFC-DPL Articles 26-31 (international transfer restricted)
  ❌ Privileged communications
  ❌ Sensitive commercial / M&A / regulatory submissions

The publisher (wolfgang_rush) is NOT in this data path. You contract directly
with [VENDOR] under their terms of service.
```

For client matters: stay on Option A (local-only).

---

*References LEGAL_EXPOSURE_PLAYBOOK §2(a) (Local-AI-Only Default pillar), §3.V4 (Data Protection — PDPL + DIFC-DPL). Playbook v0.1.*
---

## ⚠️ Third-party CLI tools and IDEs — user assumes all risk

If you integrate this Software with **any third-party AI service, CLI tool, or AI-assisted IDE** — including but not limited to: **Anthropic Claude API · Claude CLI · Claude Code · OpenAI API · Codex CLI · Google Gemini API · Gemini CLI · DeepSeek API · OpenCode · Cursor · GitHub Copilot · JetBrains AI · Mistral · Cohere · HuggingFace inference · Groq · Together AI · Qwen API · or any other model provider, CLI, IDE, or AI-assisted tool** — you do so **at your own risk** and under the terms of service of that third-party tool.

The publisher (wolfgang_rush · Rushikesh R. Mahajan):

- Does **NOT** recommend any specific third-party tool
- Does **NOT** receive any compensation, referral fee, or benefit from any third-party tool's adoption
- Does **NOT** verify any third-party tool's privacy posture, security, or compliance with your jurisdiction's law
- Accepts **NO** responsibility for your choice of third-party tooling
- Accepts **NO** responsibility for any data leakage, confidentiality breach, professional-conduct violation, regulatory non-compliance, or any other harm resulting from your use of third-party tools alongside this Software
- Makes **NO** warranty that any third-party tool is suitable for legal-professional use in any jurisdiction

**You are solely responsible** for:

- Reading the privacy policy and terms of service of each third-party tool before connecting it
- Ensuring compliance with all confidentiality rules, data-protection laws, sectoral regulations, and bar conduct rules that apply to your practice
- Obtaining client consent where required before routing client data through any third-party tool
- Verifying that the third-party tool does not retain, train on, or share your queries in ways that breach your professional obligations
- Managing API keys, access tokens, and credentials securely (do not commit them to version control; use environment variables or a password manager)
- Independently verifying any output produced by a third-party tool before client-facing use

**This warning applies regardless of which third-party tool you choose, and regardless of any privacy claim that tool makes.** The responsibility to verify and the liability for use rest entirely with you.

---

