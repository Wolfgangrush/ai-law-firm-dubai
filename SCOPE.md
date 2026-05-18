# SCOPE — AI Law Firm · Dubai-DIFC · Solo · v0.1

## In scope (v0.1 must-haves)

- [x] Forked from mempalace-3.0.0 (MIT)
- [x] Package renamed to `ailawfirm_dubai`
- [x] Dual-system package layout: `core/difc/` + `core/mainland/`
- [x] pyproject.toml v0.1.0 with Dubai-DIFC metadata
- [x] README with dual-system explanation + 5-language banner
- [x] SCOPE.md (this file)
- [x] KNOWLEDGE_PROVENANCE.md (hallucination firewall, 35 research files cited)
- [x] `ontology.py` — DIFC + Mainland matter types, court hierarchy, statute registry, bar rules
- [x] MCP tool 1: `dubai_court_lookup` (8 court stubs — 4 DIFC + 4 Mainland)
- [x] MCP tool 2: `dubai_citation_validator` (DIFC + Mainland citation formats)
- [x] MCP tool 3: `dubai_calendar_sync` (ICS, Asia/Dubai UTC+4, no DST)
- [x] Brain classifier (11 intents, including SYSTEM_SWITCH)
- [x] 7 specialist agents (including compliance_agent + system_switch_agent)
- [x] Test suite covering ontology + brain + all 3 MCP tools
- [x] MCP server wired with 3 Dubai tools
- [x] 5-language onboarding guides
- [x] CLI with dual-system banner + --system flag
- [x] All tests passing
- [x] ruff check + format both clean
- [x] Local commits clean

## Explicitly out of scope (NOT v0.1)

- [ ] Firm mode (multi-advocate, roles, billing) — v0.2+
- [ ] Real statute text (DIFC Contract Law, UAE Civil Code, DPL, etc.) — needs source PDFs · v0.2+
- [ ] Drafting templates — these live in Wolfgang_rush plugin family · separate repo
- [ ] Citation lookup against actual databases (DIFC Courts portal, UAE MoJ) — v0.3+
- [ ] Live cause-list scraping (DIFC e-registry, Dubai Courts CMS/Salif) — v0.3+
- [ ] Client billing module — v0.2+
- [ ] GitHub publish — requires RSH verification + decision · post-v0.1
- [ ] Production deployment — requires hardening · post-v0.1
- [ ] UI (terminal or web) — beyond CLI stubs · post-v0.1
- [ ] Cloud sync — explicitly anti-goal · local-first by design
- [ ] AI generation of legal advice — UAE Legal Profession Law firewall · forbidden permanently
- [ ] goAML API integration — v0.3+
- [ ] UAE PASS digital identity integration — v0.2+

## Verification path

v0.1 is verified by the publisher (Rushikesh R. Mahajan) before any GitHub publish.

## Falsification

If v0.1 cannot achieve all "in scope" items in a single DeepSeek build session of < 90 minutes, the scope or the plan is wrong. Halt and report — do not pad the scope to declare victory.
