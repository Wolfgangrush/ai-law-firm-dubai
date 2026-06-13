# 🇦🇪 AI Law Firm — Dubai-DIFC · Solo Edition

> **Free dual-system practice OS for every Dubai solo lawyer. DIFC offshore (common-law, English) + Dubai Mainland (civil-law, Arabic) — in one terminal-native tool. Local-first by default (Ollama + Qwen3 — nothing leaves your laptop). Cloud-LLM optional with the [Pseudonymisation Gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) sanitising PII before any prompt leaves the machine; UAE PDPL Article 22 + DIFC-DPL Article 26 cross-border-transfer obligations remain YOUR responsibility for any cloud-mode use.**

**For registered legal professionals only.** Intended for lawyers registered with the DIFC Courts Academy of Law (for DIFC matters), lawyers registered with the UAE Ministry of Justice (for onshore matters), foreign lawyers with DIFC rights of audience under Practice Direction 3 of 2018 or analogous provisions, in-house counsel of UAE entities, and paralegals working under their supervision. **If you are not a registered legal professional, do not use this tool to produce client-facing legal work.** Read [DISCLAIMER.md](DISCLAIMER.md) before installation.

**Version:** 0.1.1 · **License:** MIT · **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). NOT registered in the UAE (DIFC or onshore). This is a software publication for UAE-registered practitioners. · **Engine:** Built on [MemPalace](https://github.com/mempalace/mempalace) (highest-scoring open-source AI memory system · 96.6% LongMemEval R@5)

> ⚠️ **AI can make mistakes. Always verify the output.**
>
> This software generates assistive drafts and suggestions only. Every legal claim, citation, statute reference, procedural step, deadline calculation, and ground of relief must be independently verified by a qualified human practitioner before filing, advising a client, or relying on the output. The publisher accepts no liability for outputs used without verification.

> 🛡️ **Privacy primitive: PII pseudonymisation** via [pseudonymisation-gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway) (wolfgang_rush · MIT). This firm uses the `uae` jurisdiction module + Indian-diaspora overlay for cross-jurisdiction PII coverage. Open-source · zero runtime deps · session-scoped · in-memory only · never writes PII to disk.


> 🛡️ **Pseudonymisation coverage (v0.1.1):** The privacy gateway pseudonymises PII before any cloud-API call; any residue the scanner can't fully resolve is surfaced to you and audit-logged — you retain the final call (v0.3 honest-disclosure). Covers UAE-native identifiers (Emirates ID · Trade License · DIFC Court case numbers · UAE phone numbers · AED amounts · UAE IBAN) and Indian-diaspora identifiers (Aadhaar · PAN · GSTIN · IFSC · Indian phone — Dubai has ~3.4M Indian residents, so these are essential for Indian-expat client matters). Generic patterns (email · names with honorifics · dates · case numbers) work cross-jurisdiction. Mainland UAE Federal court case-number formats and additional Cassation-specific patterns will expand in v0.2.

> **🧠 AI Law Firm that LEARNS.** Every session makes the next one smarter. Two built-in Claude Code skills power this: `/retrospective` saves what the firm learned at session end — every jurisdiction, statute, argument pattern, and procedural rule you touched is logged so the firm's knowledge compounds. `/wake` loads that accumulated context the next time you start, so you never begin from zero. The firm is your second brain, and it gets sharper with every case.

---

## 🌐 Choose your language

| Script | Language | Audience | Guide |
|---|---|---|---|
| 🇬🇧 | **English** | DIFC working language · default | [GETTING_STARTED.md](GETTING_STARTED.md) |
| 🇦🇪 | **العربية (Arabic)** | Onshore Mainland · native quality | [GETTING_STARTED_ARABIC.md](GETTING_STARTED_ARABIC.md) — RTL |
| 🇵🇰 | **اردو (Urdu)** | Pakistani expat lawyers | [GETTING_STARTED_URDU.md](GETTING_STARTED_URDU.md) — RTL |
| 🇮🇳 | **हिन्दी (Hindi)** | Indian expat lawyers | [GETTING_STARTED_HINDI.md](GETTING_STARTED_HINDI.md) |
| 🇵🇭 | **Tagalog** | Filipino legal-support workforce | [GETTING_STARTED_TAGALOG.md](GETTING_STARTED_TAGALOG.md) |

> 🙏 **Honest note:** Arabic is native-quality (Mainland working language). Urdu / Hindi / Tagalog were AI-assisted to serve the Gulf expat community. **Native-speaker PRs warmly welcome** via [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md).

---

## 💛 Why this exists

> Dubai's legal market has a unique structural challenge: **One City, Two Systems.**
> - **DIFC** = English common-law system · DIFC Courts (CFI · CA · Cassation · SCT) · English working language · DIFC Contract Law · DIFC Companies Law · DIFC Employment Law · DIFC Data Protection Law (DPL)
> - **Mainland** = UAE civil-law system · Dubai Courts (CFI · CA · Cassation) + Reconciliation and Dispute Courts (RDC) · Arabic working language · UAE Civil Code · Commercial Code · Penal Code · Federal Data Protection Law 45/2021
>
> Most international firms specialize in DIFC or Mainland. Solo practitioners often serve clients in **both systems** but lack tooling that handles the dual-system reality:
> - **Tranche 2 AML/CTF compliance (goAML)** applies onshore — solo firms get audited
> - **DIFC CLPD (Compulsory Legal Practitioners Development)** plus separate Mainland CPD obligations
> - **Data localisation tension** — UAE PDPL Article 22 cross-border restrictions + DIFC-DPL Articles 26-31

BigLaw firms have dual-system teams. Solo practitioners don't. We built this so a Dubai solo lawyer can have a second brain that costs **AED 0 forever**, runs locally by default (Ollama + Qwen3), knows both systems, and supports DIFC-DPL + UAE PDPL at the architecture layer — either by absence of transmission (local mode) or by Pseudonymisation Gateway sanitisation (cloud mode, with UAE PDPL Article 22 + DIFC-DPL Article 26 cross-border-transfer obligations remaining YOUR responsibility).

---

## 🧠 What's inside — specialists who live in your terminal

| # | Specialist | What they do for you |
|---|---|---|
| 🧠 | **The Receptionist (brain)** | 11-intent classifier including the unique **SYSTEM_SWITCH** intent (mid-session DIFC↔Mainland toggle). |
| 🔀 | **The System-Switch Agent** | Detects which system the user's working in. DIFC = common-law mode. Mainland = civil-law mode. Switch via `--system` flag or natural language. |
| 📂 | **The Matter Manager** | Holds every active matter — parties, prayers, hearings, orders, draft state. Knows which system (DIFC / Mainland). |
| 📜 | **The Citation Clerk** | Parses **both DIFC formats** (`[2024] DIFC CFI 042` · `[2023] DIFC CA 015`) **and Mainland formats** (Cassation case numbers · Dubai Court case references). |
| 🏛️ | **The Court Registrar** | Knows both systems: **DIFC** (CFI · CA · Cassation · SCT) + **Mainland** (Dubai CFI · CA · Cassation · RDC). Plus shared-jurisdiction rules under Decree 19 of 2016. |
| ✍️ | **The Drafting Assistant** | Ships with **81 dual-track drafting templates** in [`_drafting_data/`](_drafting_data/) covering DIFC (English common law) + Mainland (Arabic civil law) + SHARED + FOREIGN-LAW-PRACTICE. DIFC track (RDC-based): contracts (sale of goods · employment · shareholders · NDA · lease · services) · pleadings + motions (statement of claim · defence · counterclaim · summary judgment · injunction · strike-out · joinder · extension of time) · injunctions (freezing Mareva RDC 25.27 · without-notice) · disclosure (RDC Part 28 list of documents · privilege log · specific disclosure 28.30) · expert evidence (RDC Part 31 + joint meeting) · default judgment (RDC Part 13) + set aside · enforcement (RDC Part 45 execution · Part 49 TPDO · Part 50 charging order + DIFC-Dubai Protocol) · trial documentation (bundle · chronology + cast list + reading list · written closing) · WP/Calderbank/RDC Part 36 · insolvency (DIFC Insolvency Law No. 1/2019) · DIFC Small Claims Tribunal (RDC Part 53). Mainland track (Arabic civil law): contracts (sale of goods · employment · shareholders · NDA · lease · distribution · agency) · pleadings + motions (statement of claim · defence · counterclaim · precautionary attachment · joinder · extension of time) · disclosure under Federal Decree-Law 42/2022 · court-appointed Expert (Khabir) · default judgment + opposition (المعارضة) · Dubai Courts Execution Court · Foreign Judgment Recognition (GCC + reciprocity) · hearings memorandum (مذكرة الجلسة) · Federal Court administrative judicial review (Federal Law 17/1978) · Bankruptcy (Federal Decree-Law 51/2023) · Labour Court (FDL 33/2021 + 9/2024 + MoHRE conciliation) · Real Estate Disputes (RDSC). SHARED: counsel brief to DIFC counsel + Mainland advocate · advice on merits · mediation position statement + agreement + Singapore Convention settlement (UAE acceded March 2021) · settlement agreement · arbitration clause · board resolution · DIAC Rules 2022 (post-2021 merger) + Award Set-Aside/NYC enforcement. |
| 🛡️ | **The Compliance Officer** | Watches your published material for **DIFC Code of Conduct** (DIFC practitioners) + **UAE Legal Profession Code** (Mainland practitioners) publicity firewall. Flags **goAML** Tranche 2 AML obligations, UAE PDPL Article 22 cross-border concerns, DIFC-DPL Article 26 issues. |
| 📅 | **The Calendar Sync** | ICS feed sync to iPhone Calendar / Google Calendar / Outlook — no third-party API. code-aliased summary line (lock-screen safe). Timezone Asia/Dubai (UTC+4, no DST). |

---

## 🚀 Install in 30 minutes

### Step 1 — Pick your operating system

| OS | Guide |
|---|---|
| 🍎 **Mac** | Standard Python install (Terminal) |
| 🪟 **Windows** | PowerShell · standard pip install |
| 🐧 **Linux** | Same commands as Mac |

### Step 2 — Install Python (one-time) + the tool

```bash
pip install git+https://github.com/Wolfgangrush/ai-law-firm-dubai.git
```

### Step 3 — Pick your system + Connect an AI brain

```bash
# Initialize for your practice
ailawfirm-dubai init ~/matters --system difc       # DIFC offshore only
ailawfirm-dubai init ~/matters --system mainland   # Mainland onshore only
ailawfirm-dubai init ~/matters --system both       # Dual-system practice

# Connect local AI (ONE COMMAND)
ailawfirm-dubai connect-local
```

The connect-local command:
1. Detects if Ollama is installed; if not, prints platform-specific install instructions
2. Detects your laptop's RAM
3. Recommends and downloads the right Qwen3 model (14b for 16GB+ · 7b for 8GB · 1.7b for older laptops)
4. Writes config so all subsequent calls route to local Ollama
5. Runs a smoke test to confirm local connectivity

After this, **no queries leave your laptop**.

Three honest model options — see [MODEL_SETUP.md](MODEL_SETUP.md):

| Choice | Cost | Privacy | Best for |
|---|---|---|---|
| 🥇 **Local Ollama + Qwen3** | AED 0 forever | 🟢 Perfect — nothing leaves your laptop · UAE PDPL Article 22 + DIFC-DPL Article 26 not triggered (no cross-border transfer occurs) | **Client matters · UAE PDPL Article 22 cross-border-restricted data · DIFC-DPL Articles 26-31 international-transfer-restricted data · use this tier when zero cross-border data flow is required** |
| 🥈 **DeepSeek API** | ~AED 8-20/mo | ⚠️ Pseudonymisation Gateway sanitises Emirates ID/Trade License/case references/Aadhaar + names before transmission, BUT China is NOT on UAE Data Office adequate-jurisdiction list; PDPL Article 22 cross-border safeguards still apply to the pseudonymised transmission | Non-client work · public-law research · templates |
| 🥉 **Claude / Gemini API** | ~AED 80-300/mo | 🟢 Strong (enterprise privacy default-ON) — Gateway sanitises before transmission | Heavy daily users with executed PDPL Article 22 safeguards + DIFC-DPL Article 26 standard contractual provisions or DIFC Commissioner's adequacy determination. Gateway sanitisation supports your Article 22 safeguard posture but does NOT discharge the standard contractual clause / adequacy / consent obligation. |

### Step 4 — Run

```bash
ailawfirm-dubai
```

Sample commands:

```
> tell me about DIFC SCT pecuniary jurisdiction (Small Claims Tribunal)
> validate [2024] DIFC CFI 042
> check this advert: "Best Dubai litigator · DIFC + Mainland"
> what's the goAML reporting threshold under Tranche 2?
> switch to mainland system
> add hearing MAT-2026-014 DIFC CFI Courtroom 3 2026-06-09 10:00 GST
> sync calendar
```

---

## 🔒 Privacy & Data Handling — what stays where

**Architecture — three pieces decide your privacy posture:**

**(1) Local-only state.** Your matters, drafts, audit logs, calendar entries, and configuration live in `~/.ailawfirm_dubai_difc/`. Never uploaded by the tool. Never synced to a third-party cloud by the tool. No telemetry. No "anonymous usage statistics." The publisher operates zero infrastructure and cannot access this folder. Verifiable via `grep -ri "telemetry\|analytics\|requests.post\|urlopen" ailawfirm_dubai/` — should return only user-initiated cloud-LLM calls.

**(2) LLM backend — you choose.** The default `connect-local` command configures Ollama + Qwen3 to run the language model on your laptop (truly nothing leaves; UAE PDPL Article 22 + DIFC-DPL Article 26 are not triggered in this configuration because no cross-border transfer occurs). If you opt into a cloud-LLM tier (DeepSeek / Claude / Gemini) for quality reasons, see the tier table above for cost + privacy trade-offs.

**(3) Pseudonymisation Gateway — always-on for cloud mode.** When you configure a cloud-LLM provider in `~/.ailawfirm_dubai_difc/config.json`, the internalised `PseudonymisationGateway` (source: `ailawfirm_dubai/pseudonymisation.py`) automatically substitutes real names, government IDs (Emirates ID · Trade License · Aadhaar for Indian-diaspora matters), contact identifiers (phone · email), and case references (DIFC CFI/CA/Cassation/SCT numbers · Mainland Dubai Court file numbers) with deterministic placeholders BEFORE the prompt leaves your machine. The placeholder ↔ original map lives in memory only (never written to disk; destroyed when the gateway goes out of scope). Cloud vendors see only the abstract structure of the matter; the user sees real values restored in the response.

**⚠️ UAE PDPL Article 22 + DIFC-DPL Article 26 in cloud mode.** Both regimes restrict cross-border transfer of personal data. Gateway sanitisation supports your safeguard posture (the data crossing the border is structurally pseudonymised — meaningful technical measure) but does NOT discharge:
- **Federal Decree-Law 45/2021 Article 22** — requires either (a) adequate-jurisdiction destination per UAE Data Office determination, OR (b) standard contractual provisions, OR (c) explicit consent, OR (d) other lawful basis under Article 22.
- **DIFC-DPL 5/2020 Articles 26-31** — requires either (a) DIFC Commissioner adequacy decision, OR (b) standard contractual provisions, OR (c) other lawful basis under DIFC-DPL.

For matters touching DIFC-DPL "restricted personal data" (Article 9 special categories: racial/ethnic origin · political opinions · religious beliefs · trade union membership · genetic/biometric data · health data · sex life/sexual orientation · criminal convictions) AND/OR Mainland-side health, financial, biometric, or criminal data under PDPL Article 9, additional consent + safeguards apply — consider Local Ollama tier for those matters.

**DIFC vs Mainland system contamination** — the `system_switch_agent` prevents accidental DIFC-Mainland blending in matter context. The dual-system tag enforced from matter-creation forward is independent of the dual-mode privacy architecture; both apply.

**goAML Tranche 2 AML** + **DIFC Code of Conduct (DIFC practitioners)** + **UAE Legal Profession Code (Mainland practitioners)** all apply atop the dual-mode privacy architecture. The Compliance Officer agent flags applicable regimes based on matter context.

The wedge: every other cloud-AI legal tool sends raw client PII to the LLM by default. wolfgang_rush AI Law Firm — Dubai-DIFC ships Ollama-first AND ships the Gateway as the privacy primitive that closes the gap when you choose cloud mode for quality reasons — while remaining honest that PDPL Article 22 / DIFC-DPL Article 26 / DIFC Article 9 / Mainland PDPL Article 9 obligations remain yours to execute.

### What goes to the API provider during each query

Each time the firm reasons about a matter, the following are sent to your chosen API provider:
- Your prompt (the question or instruction)
- Relevant context the firm pulls from your local matter folder (current draft state, recent orders, citations being verified)

Your full matter history, audit logs, and unrelated cases are NOT sent. The firm sends the minimum context needed to answer the current question.

### What API providers contractually guarantee

| Provider | Trains on your data? | Retention | Source |
|---|---|---|---|
| **Claude API** (Anthropic) | ❌ No — Commercial Services data is not used for training | ~30 days for safety/abuse review (Zero Data Retention available on enterprise contract) | [Anthropic Privacy Policy](https://www.anthropic.com/legal/privacy) · [Commercial Terms](https://www.anthropic.com/legal/commercial-terms) |
| **OpenAI API** (GPT-4) | ❌ No — API data not used for training since March 2023 | ~30 days for abuse review (ZDR available) | [OpenAI API Data Usage Policies](https://openai.com/policies/api-data-usage-policies) |
| **Gemini API (paid via Vertex AI)** | ❌ No — paid-tier API data not used for training | Per Google Cloud contract | [Vertex AI data governance](https://cloud.google.com/vertex-ai/docs/general/data-governance) |
| **Gemini Free Tier** | ⚠️ **YES — Google AI uses free-tier prompts to improve products** | — | [Google AI Studio terms](https://ai.google.dev/gemini-api/terms) — **DO NOT use free-tier Gemini for confidential client matters.** |
| **DeepSeek V4 Pro API** | ❌ No — per DeepSeek API terms, inputs/outputs not used for model training | Retention policy less documented than OpenAI/Anthropic; verify for matter sensitivity | [DeepSeek API ToS](https://platform.deepseek.com/api-docs/legal) · **Note:** provider is China-based; consider jurisdictional data-residency requirements |

### What that does NOT mean — solicitor's residual risk

Even though API data is not used for training:

1. **Data IS in transit** during each query — it passes through the provider's infrastructure
2. **Brief logging retention** (typically 30 days) means the provider holds the data for that window
3. **Lawful access requests** — a subpoena, lawful intercept warrant, PDPL data-subject access request, or provider security incident could expose data during the retention window
4. **Provider-side breach risk** — however small, it exists

This is fundamentally different from local-LLM mode (where no data leaves your machine, ever, period). The `connect-local` command already configures Ollama + Qwen3 as the v0.1 default — solicitors handling confidential, privileged, or special-category data should stay in local-LLM mode for that work. The cloud-LLM tier exists for non-confidential research, public-law analysis, and template scaffolding where contractual no-training is a sufficient safeguard.

### Solicitor's decision

If your matter is:
- **General commercial / corporate / contract drafting** → Claude / OpenAI / paid Gemini API are appropriate. Contractual no-training protections are strong. Audit logs are local.
- **Legal-privileged client communication / privileged litigation strategy** → Evaluate against your jurisdiction's professional conduct rules. Most regulators permit reasoned use of cloud-AI with disclosure to the client. (See Dubai (DIFC / DFSA) guidance.) Document the choice in your audit log.
- **PDPL special-category data / health / criminal record / political opinion** → Stay in `connect-local` (Ollama + Qwen3) mode. Do not opt into any cloud-LLM tier for these matters; do not use free-tier Gemini.
- **State secrets / classified material / under-seal court orders** → Stay in `connect-local` (Ollama + Qwen3) mode. For physically air-gapped networks where the pip-install / model-download / auto-update paths are also prohibited, await the v0.3+ signed offline-install bundle below.

The firm's audit log captures every API call (timestamp, agent, prompt-summary, output-summary) at `~/.ailawfirm_dubai_difc/audit_logs/`. Logs never leave your machine. They are your professional-conduct compliance trail.

### v0.3+ roadmap

> What v0.1 already ships: (a) local-LLM default via `connect-local` (Ollama + Qwen3 — nothing leaves your laptop in local mode), (b) configurable cloud-LLM tier covering Claude / OpenAI / paid Gemini / DeepSeek, (c) Pseudonymisation Gateway sanitising PII before any cloud-LLM call, and (d) no first-party telemetry. The items below extend the floor — they are not a future replacement for what is already shipped.

- **Signed offline-install bundle** — the `pip install` path currently touches PyPI and the Ollama model registry; v0.3+ ships a signed offline-installable archive with the Qwen3 model pre-bundled, removing the last network-touch point even at install time. For solicitors on physically air-gapped networks (under-seal court matter rooms, state-secret-clearance environments).
- **In-firm LLM tenant adapter** — drop-in config for Azure OpenAI / private Vertex / on-prem vLLM endpoints. Distinct from the today-shipped public-API cloud-LLM tier; targets solicitors whose firm already provisions LLM infrastructure under its own DPA.
- **Expanded local-model surface** — Llama 3.3 70B / Qwen 2.5 72B / DeepSeek V4 Pro (open-weights via Ollama), for solicitors with larger laptops who want better-than-Qwen3-14b local reasoning.

Tracked at: [drafting-agents-core issues](https://github.com/Wolfgangrush/drafting-agents-core/issues).

---

**No agenda · no telemetry · no cloud-default · MIT licensed · AED 0 forever.**

**Dubai (DIFC / DFSA) Rule compliance built into the tool's audit + transparency-gate architecture.** Solicitor remains professionally responsible for every output. The firm is a force-multiplier, not a substitute for judgment.

---

## 📁 Where your data lives

```
~/.ailawfirm-dubai/                  ← Mac/Linux
C:\Users\YourName\.ailawfirm-dubai\  ← Windows
├── palace/                          ← all matter/client/citation memory (ChromaDB)
├── config.json                      ← your settings (AI provider · system · timezone · prefs)
├── calendars/                       ← generated .ics feeds for iPhone/Outlook subscribe
└── people_map.json                  ← optional client alias system (lock-screen safety)
```

Copy this folder to a USB drive · OneDrive · iCloud Drive · Dropbox = complete backup of your practice in 5 seconds.

---

## 🔄 How to update your firm

When a new version of AI Law Firm — Dubai · DIFC is published, you pull it in with **one command**. Your matter data + your project-root `CLAUDE.md` are **never touched** — only the firm's installed code, skills, and prompts refresh.

### Path 1 — Plain terminal

```
ailawfirm-dubai update
```

Under the hood this runs `pip install --upgrade git+https://github.com/Wolfgangrush/ai-law-firm-dubai.git`. After it finishes, restart any open `ailawfirm-dubai` session so the new skills + prompts load.

### Path 2 — Inside Claude Code

Type:

```
/update
```

Claude runs the same command for you and reports the result.

### Path 3 — Inside Gemini CLI

Type:

```
/update
```

Same outcome — Gemini calls `ailawfirm-dubai update` for you.

### When to update

- **The publisher tells you** a new version is out → update.
- **Monthly hygiene** → update once a month so you stay current on skills + bug fixes.
- **After hitting a bug** → first thing to try is updating, in case it is already fixed upstream.

### What does NOT update (by design)

- Your matter folders (`~/Desktop/<your-firm>/<matter>/...`)
- Your project-root `CLAUDE.md` (your customisations always win)
- Your `~/.ailawfirm-dubai/` config + palace data
- Your chosen AI model setup (Ollama · DeepSeek · Claude · Gemini)

Only the firm's installed Python code, skills, and template files refresh. Your practice is unaffected.

### One catch — existing users + new template rules

If a new version updates the template `CLAUDE.md` (the firm's standing rules), your project-root `CLAUDE.md` is preserved because your customisations always win. To see what changed in the template after an update:

```
diff CLAUDE.md "$(python3 -c 'import ailawfirm_dubai, os; print(os.path.join(os.path.dirname(ailawfirm_dubai.__file__), "templates/CLAUDE.md"))')"
```

Review the diff and merge what you want into your own `CLAUDE.md`.

---

## 🛤️ Roadmap (honest)

> 🙏 **Honest note on timelines:** Solo-author OSS · ships as time permits · v0.2 / v0.3 / v0.4+ targets are indicative, not committed dates. Open an issue if a specific feature on a specific timeline matters to your work.



- **v0.1.0** *(shipped)* — bootstrap: dual-system ontology · 11-intent brain (with SYSTEM_SWITCH) · 7 specialist agents (4 live · 3 stubs) · 3 working MCP tools (court · citation · calendar) · 5-language onboarding (English · Arabic · Urdu · Hindi · Tagalog) · connect-local one-command CLI · LEGAL_EXPOSURE_PLAYBOOK v0.1 compliance
- **v0.2 — knowledge layer** *(shipped 2026-05-28)* — **81 dual-track drafting templates** in `_drafting_data/` covering DIFC + Mainland + SHARED + FOREIGN-LAW-PRACTICE: (a) DIFC contracts + pleadings + motions + court forms; (b) Mainland contracts + pleadings + motions + court forms; (c) **full 13-category litigation backbone** across both systems where applicable — disclosure dual-track (DIFC RDC Part 28 + Mainland FDL 42/2022) · expert evidence dual-track (DIFC RDC Part 31 + Mainland Khabir) · default judgment dual-track (DIFC + Mainland) · enforcement dual-track (DIFC Execution + TPDO + Charging Order + DIFC-Dubai Protocol; Mainland Execution Court + Foreign Judgment Recognition) · DIFC injunctions (freezing Mareva + without-notice) · counsel briefing SHARED · Mainland Federal Court judicial review · DIFC trial documentation (bundle + chronology + closing) · Mainland hearings memorandum · ADR SHARED (mediation + Singapore Convention + WP/Calderbank/RDC Part 36) · dual-track insolvency (DIFC Insolvency Law 2019 + Mainland FDL 51/2023) · tribunals (DIFC SCT + Mainland Labour MoHRE + RDSC Real Estate) · DIAC arbitration + Award Set-Aside/NYC enforcement.
- **v0.2 — statute knowledge layer** *(shipped 2026-05-29)* — **24 statute digests** in `_statute_corpus/` covering the full dual-track backbone: (a) **15 DIFC** instruments — Contract Law 2004 · Employment Law 2019 · Companies Law 2018 · Data Protection Law 2020 · Insolvency Law 2019 · Arbitration Law 2008 · Court Law 2004 · RDC Rules · Regulatory Law 2004 · Law of Obligations 2005 · Personal Property Law 2005 · Real Property Law 2018 · Trust Law 2018 · Digital Assets Law 2024 · Conflicts Decree 19/29; (b) **9 Mainland UAE Federal** instruments — Civil Code (Federal Law 5/1985) · Commercial Code (FDL 50/2022) · Civil Procedure Law (FDL 42/2022) · Penal Code (FDL 31/2021) · Evidence Law (FDL 35/2022) · Labour Law (FDL 33/2021) · Commercial Companies Law (FDL 32/2021) · Personal Data Protection Law (FDL 45/2021) · AML Law (FDL 20/2018, 2025 amendments).
- **v0.1.1 — Pseudonymisation Gateway** *(shipped 2026-05-29)* — internalised at `ailawfirm_dubai/pseudonymisation.py`; sanitises PII before any cloud-LLM call. Standalone source at [pseudonymisation-gateway](https://github.com/Wolfgangrush/pseudonymisation-gateway).
- **v0.2 — frontend / UX layer** *(in progress)* — matter dashboard · goAML reporting helper
- **v0.3** *(following milestone)* — **firm mode** for multi-lawyer dual-system practices · role/permission · conflict-check across systems · trust-account / client-account compliance · Decree 19 of 2016 shared-jurisdiction handling
- **v0.4+** — DIFC Courts website / UAE Federal Legal Gazette cross-reference · ADGM bridge (Abu Dhabi) · Apple EventKit native · CalDAV bidirectional sync · deeper Cassation precedent search · Federal Cassation Court templates · DIFC Wills + Probate · Family / Personal Status Court (Sharia) · Mainland Property Law beyond RDSC

Six sister jurisdictions on the same architecture: 🇮🇳 India · 🇸🇬 Singapore · 🇬🇧 UK · 🇦🇺 Australia · 🇪🇺 EU · 🇺🇸 USA — each as its own MIT-licensed repo.

---

## 🌐 Family Status (honest · cross-firm)

The wolfgang_rush AI Law Firm family ships across 7 jurisdictions. Honest status of the v0.2 legal-knowledge layer (statute corpus + drafting data) per firm:

| Firm | Statute corpus | Drafting corpus | Shared agents | GitHub |
|------|---|---|---|---|
| 🇮🇳 **India** | Native knowledge base · maintainer-curated | wolfgang_rush plugins (14 Indian-litigation plugins · separate stack) | Not applicable — Indian-specific | ✅ LIVE |
| 🇪🇺 **EU** | ✅ 11 statutes · 8/8 Tier-1 | ✅ **56 templates** · litigation + commercial complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇺 **Australia** | ✅ 13 Tier-1 statute digests + 39 research files | ✅ **79 templates** · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇦🇪 **Dubai-DIFC** | ✅ 24 statute digests · dual-track (15 DIFC + 9 Mainland UAE Federal) · v0.2 closed 2026-05-29 | ✅ **81 templates** · dual-track DIFC + Mainland · litigation + commercial + tribunal complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇸🇬 **Singapore** | ✅ 17 statute digests Tier-1 | ✅ **55 templates + 6 scaffolds** · litigation + commercial + regulatory complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇬🇧 **UK** | ✅ 10 statute digests Tier-1 | ✅ **107 templates** · litigation + commercial + Tier-3 specialist + procedural anchors complete (v0.2 closed 2026-05-28) | ✅ Migrated | ✅ LIVE |
| 🇺🇸 **USA** | ✅ 23 federal-first Tier-1 statute digests | ✅ **89 templates** · all 13 litigation categories + commercial + corporate complete (v0.2 closed 2026-05-29) | ✅ Migrated | ✅ LIVE |

**Plus:**
- **AI Startup Firm — India v0.1** (legal-ops brain for founders)
- **GC In-House Brain** (multi-jurisdictional, 8 modules — 3 live · 5 shipping v0.2+)

Both share the same `drafting-agents-core` architecture pattern.

All firms migrated to the central [drafting-agents-core](https://github.com/Wolfgangrush/drafting-agents-core) agent library on 2026-05-20 (Path B-Lite) — single source of truth for the agent layer; jurisdictional knowledge stays per-firm.

---

## 📚 Documentation

| File | What it covers |
|---|---|
| [GETTING_STARTED.md](GETTING_STARTED.md) + 4 language variants | Layman-friendly 30-minute tour |
| [DISCLAIMER.md](DISCLAIMER.md) | Full legal disclaimer · DIFC + Mainland dual-system positioning · UAE PDPL + DIFC-DPL · UPL exclusion |
| [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md) | Zero-collection architecture · UAE PDPL Article 22 · DIFC-DPL Articles 26-31 international transfer analysis |
| [SECURITY.md](SECURITY.md) | Vulnerability reporting · coordinated disclosure · security hygiene |
| [MODEL_SETUP.md](MODEL_SETUP.md) | Honest privacy table · local vs cloud · third-party CLI tool warning |
| [SCOPE.md](SCOPE.md) | What's in v0.1, what's not |
| [KNOWLEDGE_PROVENANCE.md](KNOWLEDGE_PROVENANCE.md) | Every domain claim's source (CITED:<research-file>) |

---

## 🙏 Credits

- **Engine — all architectural credit:** [MemPalace](https://github.com/mempalace/mempalace) — the highest-scoring open-source AI memory system ever benchmarked. MIT licensed. We are a downstream fork specialized for Dubai dual-system practice.
- **Publisher:** [wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (High Courts of India, India). MIT-licensed legal-tech publisher.
- **Inspired by:** every Dubai solo lawyer who's worked Friday-night switching between DIFC English-language pleadings and Mainland Arabic-language submissions.

---

## ⚠️ Disclaimer

This tool helps you organize your practice. It does **NOT** give legal advice. It does **NOT** replace your professional judgment. It does **NOT** solicit work on your behalf. DIFC Code of Conduct + UAE Legal Profession Code publicity firewalls are built in but **YOU** remain responsible for compliance with all bar conduct rules, UAE PDPL, DIFC-DPL, goAML/AML-CTF obligations, and DIFC Court Practice Directions.

The publisher is not registered in the UAE (DIFC or onshore). The publisher does not offer legal services in the UAE. This is a software publication under the MIT License.

Ships AS-IS without warranty. See [LICENSE](LICENSE).

---

## 📞 Support

- **Issues / bugs:** https://github.com/Wolfgangrush/ai-law-firm-dubai/issues
- **Translation help:** [TRANSLATION_HELP_WANTED.md](TRANSLATION_HELP_WANTED.md) (Arabic native-PR · Urdu · Hindi · Tagalog welcome)
- **DIFC-specific feature request?** Open an issue with `[difc]` label
- **Mainland-specific feature request?** Open an issue with `[mainland]` label

---

`Let's begin. لنبدأ. آئیے شروع کرتے ہیں. चलिए शुरू करें. Magsimula tayo.` 🙏
