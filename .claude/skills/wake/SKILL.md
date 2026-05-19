---
name: wake
description: Start-of-session state loader for Dubai-DIFC AI Law Firm users. Runs 2-pass leak-check (Rule 1: same scope as retrospective — no mempalace, no AAAK, no lawtech-arc, no personal-build refs). Loads jurisdiction context so every session begins informed.
allowed-tools: Bash, Read, Glob
---

# /wake — Start-of-Session State Loader (Dubai-DIFC)

Loads the Dubai-DIFC AI Law Firm's current state at session start. Displays readiness so the user knows exactly what's available before they begin work.

## 2-Pass Leak-Check (Rule 1 — execute FIRST, before displaying state)

### Pass 1 — AAAK codes + MemPalace paths
```bash
# Detect any 2-5 letter all-caps token (potential internal matter shorthand)
grep -rniE '\b[A-Z]{2,5}\b' --include="*.md" --include="*.json" --include="*.txt" . 2>/dev/null \
  | grep -vE '\b(USA|UK|EU|UAE|HC|SC|API|JSON|MIT|MCP|CSV|PDF|XML|HTML|HTTP|URL|ABN|TFN|GST|VAT|CEO|CFO|CIO|MD|QC|SC|JD|LLM|LLB|BSc|MBA|GDP|GDPR|CCPA|DPDP|AI|ML|NLP|CLI|IDE|SDK|README|CI|CD|PR|RFC|ETA|EOD|TBD|FYI|NB|AM|PM)\b'
grep -rni 'mempalace\|\.mempalace\|--mempalace' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = flag immediately. Do not proceed silently.

### Pass 2 — Lawtech-arc + personal-build refs
```bash
grep -rni 'lawtech.arc\|lawtech_arc\|@lawtech' --include="*.md" --include="*.json" . 2>/dev/null
grep -rni 'personal.build\|Wolfgang.Rush.personal' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = flag immediately.

## Workflow

### Step 1: Run 2-pass leak-check (above)
If either pass fails, display warning before proceeding.

### Step 2: System state check
```bash
echo "Python: $(python3 --version 2>&1)"
echo "Package: $(pip show ailawfirm_dubai 2>&1 | head -3)"
echo "Data dir: $(ls -la ~/.ailawfirm-dubai/ 2>&1 | head -5)"
echo "Config: $(cat ~/.ailawfirm-dubai/config.json 2>&1 | head -10)"
```

### Step 3: Jurisdiction context
Display the Dubai-DIFC-specific legal framework:
- **DIFC Courts** (offshore, common-law, English-language) + **Dubai Mainland Courts** (onshore, civil-law, Arabic-language)
- **Statutes:** DIFC Law No. 10 of 2004, DIFC Courts Law, DIFC Data Protection Law 2020, UAE Civil Code, UAE Federal Law No. 11 of 1992 (Civil Procedure), UAE Federal Law No. 18 of 1993 (Commercial Transactions)
- **Arbitration:** DIFC-LCIA, DIAC, UAE Federal Arbitration Law (Federal Law No. 6 of 2018)
- **Regulatory:** DIFC Academy of Law, UAE Ministry of Justice, DFSA

### Step 4: Specialists available
| # | Specialist | Status |
|---|---|---|
| 🧠 | Receptionist (brain) | READY |
| 📂 | Matter Manager | READY |
| 📜 | Citation Clerk | READY |
| 🏛️ | Court Registrar | READY |
| ✍️ | Drafting Assistant | READY |
| 🛡️ | Compliance Officer | READY |
| 📅 | Deadline Tracker | READY |

### Step 5: Present readiness summary

## Output Format

```markdown
## 🇦🇪 Dubai-DIFC AI Law Firm — Ready

🟢 Leak-check: PASS (Pass 1 clean · Pass 2 clean)

**System:**
- Python: [version]
- Package: ailawfirm_dubai [version]
- Data: ~/.ailawfirm-dubai/ [status]

**7 specialists online.**
**DIFC Courts + Dubai Mainland Courts mapped. Dual-system (common-law + civil-law).**
**DIFC Data Protection Law 2020 · UAE Civil Code loaded. English + Arabic.**

🧠 This firm LEARNS. Every session makes the next one smarter.
   Run `/retrospective` at session end to save what you learned.

---
What do you need today?
```

## Anti-Pollution Rules (DO NOT BREAK)
- Never reference `~/.mempalace/` or any mempalace path
- Never use AAAK entity codes
- Never reference lawtech-arc architecture
- Never reference Wolfgang Rush personal builds

## What this skill does NOT do
- Does NOT read or write to MemPalace
- Does NOT access personal diary or KG
- Does NOT touch any other firm's directory
- Does NOT modify any file (read-only state display)
