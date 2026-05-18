# NO_PII_NO_DATA — Zero-Collection Architecture (Dubai-DIFC)

**This document explains why AI Law Firm — Dubai collects no personal data from you, and what that means under UAE Federal Decree-Law No. 45/2021 (PDPL) and DIFC Data Protection Law No. 5/2020.**

## The short version

The publisher (Wolfgang Rush) operates **zero infrastructure** that touches your data. There is no server. There is no telemetry. There is no analytics. The tool runs entirely on your laptop.

## The architectural guarantee

AI Law Firm — Dubai is **local-first** software. Specifically:

**(1) The codebase contains zero telemetry.** Verify with `grep -ri "telemetry\|analytics\|tracking\|requests.post\|urlopen" ailawfirm_dubai/`.

**(2) The publisher operates no server.** No AI Law Firm Dubai API. No cloud service. No database.

**(3) Storage is on your laptop.** Matter data, citations, calendar, configuration live under `~/.ailawfirm-dubai/`. The publisher has no access.

**(4) Network calls are limited to:**
- Package installation (PyPI)
- User-initiated cloud AI calls (direct user→vendor, never through publisher)
- Optional update checks (v0.2+ if added — opt-in only)

## Cloud-mode (when you opt in)

If you enable cloud AI, your queries route **directly from your laptop to the AI vendor**. The publisher is not in the data path. The contract is between you and the vendor. For client-confidential work or any matter touching UAE Federal data-protection obligations, use **local-only mode**. See [MODEL_SETUP.md](MODEL_SETUP.md).

## UAE PDPL (Federal Decree-Law No. 45/2021)

**The publisher is neither a Controller nor a Processor** under the PDPL with respect to your tool usage.

Article 1 defines a "Controller" as "the person/entity that determines the manner and purposes of personal data processing." The publisher determines neither. A "Processor" processes data on behalf of a Controller; the publisher processes nothing.

The publisher is a software publisher — publishing open-source software is not "processing personal data" under Article 1 PDPL.

If you use the tool to process personal data of UAE data subjects, **you** are the Controller. PDPL obligations apply:
- Lawful basis (Article 4)
- Consent (Article 6, where required)
- Data subject rights (Articles 13-19: access · correction · erasure · restriction · portability · objection)
- Breach notification to the Data Office within 72 hours (Article 9)
- DPO appointment for high-risk or large-scale processing (Article 10)
- Cross-border transfer restrictions (Article 22) — transfers permitted only to jurisdictions with adequate protection or with appropriate safeguards
- Data Protection Impact Assessment for high-risk processing (Article 21)

## DIFC Data Protection Law No. 5/2020

The DIFC-DPL applies to entities established in DIFC or processing personal data within DIFC. The publisher has no DIFC establishment and processes no data in DIFC.

If you operate a DIFC-registered practice and process personal data, your DIFC-DPL obligations apply. The DIFC-DPL is closely aligned with GDPR; obligations include:
- Lawful processing grounds (Article 10)
- Data subject rights (Articles 32-43)
- DPO appointment for certain processing (Article 16)
- DPIA for high-risk processing (Article 20)
- Breach notification to the DIFC Commissioner within 72 hours (Article 41)
- International transfer restrictions (Articles 26-31)

The tool's local-only mode keeps personal data on your DIFC-registered device, supporting DIFC-DPL compliance.

## Cross-border transfer (Article 22 PDPL / Articles 26-31 DIFC-DPL)

If you opt into cloud mode and the cloud vendor processes data outside the UAE / DIFC, the transfer is YOUR action. Your obligations apply. The publisher transfers no personal data anywhere.

## Verification path

You can independently verify zero-collection:

1. `grep -ri "telemetry\|analytics\|posthog\|mixpanel\|segment\|amplitude\|google-analytics\|datadog\|sentry" ailawfirm_dubai/`
2. `cat requirements.txt`
3. Run the tool offline
4. Inspect network traffic with `nettop` / `nethogs`

## If this changes

If a future version adds telemetry or any cloud touchpoint involving the publisher's infrastructure, the change will be announced in CHANGELOG, default OFF, opt-in only, and documented here.

---

*This document references LEGAL_EXPOSURE_PLAYBOOK §2(b) (Zero Data Collection pillar), §3.V4 (Data Protection — UAE PDPL + DIFC-DPL), §3.V9 (Conduct-Rule Inducement). Playbook version: v0.1.*
