# AI Law Firm — Dubai-DIFC · Solo Edition · v0.1

```
═══════════════════════════════════════════════════════════════════
  AI Law Firm — Dubai-DIFC · Solo Edition · v0.1

  🙏 Welcome · أهلاً وسهلاً · خوش آمدید · स्वागत · Mabuhay
═══════════════════════════════════════════════════════════════════
  DIFC (offshore common-law) + Dubai Mainland (onshore civil-law)
  Pick: ailawfirm-dubai init --system difc|mainland|both
═══════════════════════════════════════════════════════════════════
```

**Dual-system practice OS for Dubai solo advocates.** One City, Two Systems — DIFC offshore (common-law, English) + Dubai Mainland (civil-law, Arabic) — in one free, local-first tool.

Built on [MemPalace](https://github.com/mempalace/mempalace) (MIT). Published by Wolfgang Rush. $0 forever. Your data stays on your machine.

## Quick Start

```bash
# Install
pip install -e .

# Set up your practice (pick your system)
ailawfirm-dubai init ~/matters --system difc       # DIFC offshore only
ailawfirm-dubai init ~/matters --system mainland    # Dubai Mainland only
ailawfirm-dubai init ~/matters --system both        # Dual-system practice

# Mine your matters
ailawfirm-dubai mine ~/matters

# Search everything
ailawfirm-dubai search "DIFC Contract Law amendment 2024"
ailawfirm-dubai search "goAML filing deadline"
```

## What This Is

A memory OS for Dubai solo lawyers. It ingests your case files, research notes, and client communications and makes them instantly searchable. Think of it as your personal practice search engine — no cloud, no subscription, your data never leaves your machine.

**5 language guides:** English · العربية (Arabic) · اردو (Urdu) · हिन्दी (Hindi) · Tagalog — covering the Gulf legal community.

## Dual-System Architecture (ADR-005)

Dubai operates a unique "One City, Two Systems" legal framework:

| System | Law | Language | Courts |
|---|---|---|---|
| **DIFC** | Common-law | English | DIFC CFI · CA · Cassation · SCT |
| **Mainland** | Civil-law | Arabic | Dubai CFI · CA · Cassation · RDC |

The `--system` flag determines which courts, statutes, and language templates load by default. Switch mid-session via the `system_switch_agent`.

## Features (v0.1)

- **Dual-system ontology** — DIFC statutes (Contract Law, Employment, DPL, Companies, Insolvency) + UAE Federal statutes (Civil Code, Commercial Code, Penal Code, DPP, AML)
- **3 MCP tools** — `dubai_court_lookup` (8 court stubs, DIFC + Mainland), `dubai_citation_validator` (DIFC + Mainland formats), `dubai_calendar_sync` (ICS, Asia/Dubai UTC+4)
- **7 specialist agents** — matter, citation, court, drafting, deadline, compliance (goAML · DPL · CLPD · UAE DPP), system_switch
- **11 brain intents** — including SYSTEM_SWITCH for mid-session DIFC↔Mainland toggle
- **5-language onboarding** — English · Arabic (native quality) · Urdu · Hindi · Tagalog (AI-assisted)
- **Timezone-aware** — Asia/Dubai (UTC+4, no DST)

## License

MIT — see [LICENSE](LICENSE).

Built on [MemPalace](https://github.com/mempalace/mempalace) (MIT). Upstream credit: the memory architecture powering this tool.

## Language Guides

- [GETTING_STARTED.md](GETTING_STARTED.md) — English (authoritative)
- [GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md) — العربية (RTL, native quality — Mainland primary)
- [GETTING_STARTED_URDU.md](GETTING_STARTED_URDU.md) — اردو (RTL, AI-assisted — Pakistani expat)
- [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) — हिन्दी (AI-assisted — Indian expat)
- [GETTING_STARTED_TAGALOG.md](GETTING_STARTED_TAGALOG.md) — Tagalog (AI-assisted — Filipino legal-support workforce)

## Provenance

Every domain claim is tagged. See [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md) for the full claim ledger — CITED against 35 research files.

## Scope

v0.1 is intentionally minimal. See [SCOPE.md](SCOPE.md).

**Explicitly out of scope:** firm mode (multi-advocate), real statute text, drafting templates, live cause-list scraping, citation lookup against databases, billing, cloud sync.

## Verifier

Built by DeepSeek V4 Pro. To be verified by `claude-real` (Opus 4.7) running `/lawtech-code-review` before any GitHub publish.
