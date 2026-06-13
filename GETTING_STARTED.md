# GETTING STARTED — AI Law Firm · Dubai-DIFC · v0.1

```
🙏 Welcome · أهلاً وسهلاً · خوش آمدید · स्वागत · Mabuhay
```

## What is this?

A free, local-first practice OS for Dubai solo advocates. It ingests your case files, research notes, and client communications — and makes them instantly searchable. Think of it as your personal legal search engine that never leaves your machine.

**One City, Two Systems** — Dubai's unique legal landscape: DIFC offshore (common-law, English) + Dubai Mainland (onshore civil-law, Arabic) — in one tool. Pick your system at init: `--system difc`, `--system mainland`, or `--system both`.

## Installation

```bash
cd ~/ai-law-firm-dubai-difc
pip install -e .
```

## Quick Start

```bash
# 1. Set up your practice (pick your system)
ailawfirm-dubai init ~/matters --system difc       # DIFC common-law only
ailawfirm-dubai init ~/matters --system mainland    # Mainland civil-law only
ailawfirm-dubai init ~/matters --system both        # Dual-system practice

# 2. Mine your matters
ailawfirm-dubai mine ~/matters

# 3. Search everything
ailawfirm-dubai search "DIFC Contract Law amendment 2024"
ailawfirm-dubai search "goAML filing requirements"

# 4. Check status
ailawfirm-dubai status
```

## Dual-System Switch

You can switch between DIFC and Mainland mid-session:

```
"switch to DIFC"     → DIFC context (common-law, English, DIFC statutes)
"switch to Mainland" → Mainland context (civil-law, Arabic, UAE Federal statutes)
"switch to both"     → Dual-system context
```

## What v0.1 Can Do

- **Search** your matters with exact-word matching
- **Look up courts** — 8 Dubai court stubs (DIFC CFI, DIFC CA, DIFC Cassation, DIFC SCT, Dubai CFI, Dubai CA, Dubai Cassation, RDC)
- **Validate citations** — DIFC style (`[2024] DIFC CFI 234`) and Mainland style (`Case 456 2023 (Dubai CFI)`)
- **Generate calendar events** — ICS format, Asia/Dubai UTC+4
- **Flag compliance** — goAML, DPL, CLPD, UAE DPP keyword detection
- **Check deadlines** — limitation periods for civil, employment, contract, tort, rental

## What v0.1 Does NOT Do (yet)

- Draft documents (coming via wolfgang_rush plugin family)
- Look up real citations against databases
- Scrape cause lists
- Multi-advocate billing
- Cloud sync (intentionally — your data stays local)

## Language Guides

We serve Dubai's multilingual legal community:

- [हिन्दी — GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md)
- [العربية — GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md)
- [اردو — GETTING_STARTED_URDU.md](GETTING_STARTED_URDU.md)
- [Tagalog — GETTING_STARTED_TAGALOG.md](GETTING_STARTED_TAGALOG.md)

## Need Help?

Read [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) to contribute.

## License

MIT. Built on [MemPalace](https://github.com/mempalace/mempalace). Published by wolfgang_rush.
