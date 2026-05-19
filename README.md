# 🇦🇪 AI Law Firm — Dubai-DIFC · Solo Edition

> **Free dual-system practice OS for every Dubai solo lawyer. DIFC offshore (common-law, English) + Dubai Mainland (civil-law, Arabic) — in one terminal-native, local-first tool. Your data stays on your laptop.**

**For registered legal professionals only.** Intended for lawyers registered with the DIFC Courts Academy of Law (for DIFC matters), lawyers registered with the UAE Ministry of Justice (for onshore matters), foreign lawyers with DIFC rights of audience under Practice Direction 3 of 2018 or analogous provisions, in-house counsel of UAE entities, and paralegals working under their supervision. **If you are not a registered legal professional, do not use this tool to produce client-facing legal work.** Read [DISCLAIMER.md](DISCLAIMER.md) before installation.

**Version:** 0.1.0 · **License:** MIT · **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (Bombay High Court, Nagpur Bench, India). NOT registered in the UAE (DIFC or onshore). This is a software publication for UAE-registered practitioners. · **Engine:** Built on [MemPalace](https://github.com/mempalace/mempalace) (highest-scoring open-source AI memory system · 96.6% LongMemEval R@5)

> ⚠️ **AI can make mistakes. Always verify the output.**
>
> This software generates assistive drafts and suggestions only. Every legal claim, citation, statute reference, procedural step, deadline calculation, and ground of relief must be independently verified by a qualified human practitioner before filing, advising a client, or relying on the output. The publisher accepts no liability for outputs used without verification.

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

BigLaw firms have dual-system teams. Solo practitioners don't. We built this so a Dubai solo lawyer can have a second brain that costs **AED 0 forever**, runs locally, knows both systems, and respects DIFC-DPL + UAE PDPL at the architecture layer.

---

## 🧠 What's inside — specialists who live in your terminal

| # | Specialist | What they do for you |
|---|---|---|
| 🧠 | **The Receptionist (brain)** | 11-intent classifier including the unique **SYSTEM_SWITCH** intent (mid-session DIFC↔Mainland toggle). |
| 🔀 | **The System-Switch Agent** | Detects which system the user's working in. DIFC = common-law mode. Mainland = civil-law mode. Switch via `--system` flag or natural language. |
| 📂 | **The Matter Manager** | Holds every active matter — parties, prayers, hearings, orders, draft state. Knows which system (DIFC / Mainland). |
| 📜 | **The Citation Clerk** | Parses **both DIFC formats** (`[2024] DIFC CFI 042` · `[2023] DIFC CA 015`) **and Mainland formats** (Cassation case numbers · Dubai Court case references). |
| 🏛️ | **The Court Registrar** | Knows both systems: **DIFC** (CFI · CA · Cassation · SCT) + **Mainland** (Dubai CFI · CA · Cassation · RDC). Plus shared-jurisdiction rules under Decree 19 of 2016. |
| ✍️ | **The Drafting Assistant** | Connects to the Wolfgang_rush drafting plugins (separate, MIT, optional). v0.1 = connection · v0.2+ = real templates per system. |
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
| 🥇 **Local Ollama + Qwen3** | AED 0 forever | 🟢 Perfect — nothing leaves your laptop | **Client matters · UAE PDPL Article 22 cross-border · DIFC-DPL Articles 26-31 international transfer-restricted data** |
| 🥈 **DeepSeek API** | ~AED 8-20/mo | ⚠️ Acceptable IF opt-out — but China is NOT on UAE Data Office adequate-jurisdiction list; PDPL Article 22 applies | Non-client work · public-law research · templates |
| 🥉 **Claude / Gemini API** | ~AED 80-300/mo | 🟢 Strong (enterprise privacy default-ON) | Heavy daily users with executed PDPL Article 22 safeguards |

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

## 🛡️ Privacy posture (the honest version)

- **The tool itself:** your matters, clients, drafts, notes NEVER leave your laptop. Local SQLite + ChromaDB. MIT-licensed source you can audit.
- **The AI model you connect** — different story. Cloud APIs (DeepSeek · Claude · Gemini) see your queries. See [MODEL_SETUP.md](MODEL_SETUP.md) for the honest privacy table. **For actual client matters → use local Ollama. No exceptions.**
- **DIFC Code of Conduct + UAE Legal Profession Code + UAE PDPL + DIFC-DPL + goAML:** the Compliance Officer specialist checks your published language for publicity/solicitation risk, flags PDPL Article 22 cross-border concerns, surfaces Tranche 2 AML red flags. But YOU remain responsible for compliance.
- **Dual-system isolation:** matters tagged DIFC stay in DIFC mode (common-law citations, English templates) · matters tagged Mainland stay in Mainland mode (civil-law citations, Arabic templates). The system_switch_agent prevents accidental cross-system contamination.
- **Calendar sync:** ICS feed only. No Google Calendar API. No third-party data processor. Lock-screen event summaries use entity aliases.

See [NO_PII_NO_DATA.md](NO_PII_NO_DATA.md) for the complete zero-collection architecture and UAE PDPL + DIFC-DPL controller analysis.

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

## 🛤️ Roadmap (honest)

> 🙏 **Honest note on timelines:** Solo-author OSS · ships as time permits · v0.2 / v0.3 / v0.4+ targets are indicative, not committed dates. Open an issue if a specific feature on a specific timeline matters to your work.



- **v0.1.0** *(now)* — bootstrap: dual-system ontology · 11-intent brain (with SYSTEM_SWITCH) · 7 specialist agents (4 live · 3 stubs) · 3 working MCP tools (court · citation · calendar) · 5-language onboarding (English · Arabic · Urdu · Hindi · Tagalog) · connect-local one-command CLI · LEGAL_EXPOSURE_PLAYBOOK v0.1 compliance
- **v0.2** *(next milestone)* — DIFC statute text (Contract Law · Employment Law · DPL · Companies Law · Insolvency Law) · Mainland statute text (UAE Civil Code · Commercial Code · Penal Code · Federal Data Protection 45/2021) · Pseudonymisation Gateway for safe cloud-mode · matter dashboard · goAML reporting helper
- **v0.3** *(following milestone)* — **firm mode** for multi-lawyer dual-system practices · role/permission · conflict-check across systems · trust-account / client-account compliance · Decree 19 of 2016 shared-jurisdiction handling
- **v0.4+** — DIFC Courts website / UAE Federal Legal Gazette cross-reference · ADGM bridge (Abu Dhabi) · Apple EventKit native · CalDAV bidirectional sync · deeper Cassation precedent search

Six sister jurisdictions on the same architecture: 🇮🇳 India · 🇸🇬 Singapore · 🇬🇧 UK · 🇦🇺 Australia · 🇪🇺 EU · 🇺🇸 USA — each as its own MIT-licensed repo.

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
- **Publisher:** [Wolfgang_rush](https://github.com/Wolfgangrush) — an Indian advocate (Bombay HC Nagpur, India). MIT-licensed legal-tech publisher.
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
