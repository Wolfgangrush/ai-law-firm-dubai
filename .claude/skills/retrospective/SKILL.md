---
name: retrospective
description: End-of-session save discipline for Dubai-DIFC AI Law Firm users. Runs 2-pass leak-check (Rule 6: no mempalace, no AAAK, no lawtech-arc, no personal-build refs). Saves session learning so the firm gets smarter with every use.
allowed-tools: Bash, Read, Glob
---

# /retrospective — End-of-Session Save Discipline (Dubai-DIFC)

Saves what the Dubai-DIFC AI Law Firm learned this session. Runs at session end. The firm accumulates knowledge across sessions without leaking personal context.

## 2-Pass Leak-Check (Rule 6 — execute BEFORE any save)

### Pass 1 — AAAK codes + MemPalace paths
```bash
# Detect any 2-5 letter all-caps token (potential internal matter shorthand)
grep -rniE '\b[A-Z]{2,5}\b' --include="*.md" --include="*.json" --include="*.txt" . 2>/dev/null \
  | grep -vE '\b(USA|UK|EU|UAE|HC|SC|API|JSON|MIT|MCP|CSV|PDF|XML|HTML|HTTP|URL|ABN|TFN|GST|VAT|CEO|CFO|CIO|MD|QC|SC|JD|LLM|LLB|BSc|MBA|GDP|GDPR|CCPA|DPDP|AI|ML|NLP|CLI|IDE|SDK|README|CI|CD|PR|RFC|ETA|EOD|TBD|FYI|NB|AM|PM)\b'
grep -rni 'mempalace\|\.mempalace\|--mempalace' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = STOP. Do not save. Flag for manual review.

### Pass 2 — Lawtech-arc + personal-build refs
```bash
grep -rni 'lawtech.arc\|lawtech_arc\|@lawtech' --include="*.md" --include="*.json" . 2>/dev/null
grep -rni 'personal.build\|Wolfgang.Rush.personal' --include="*.md" --include="*.json" . 2>/dev/null
```
**Expected: zero hits.** Any hit = STOP.

## Workflow

### Step 1: Collect session summary
Review the current conversation for:
- Which specialists were invoked (Receptionist, Matter Manager, Citation Clerk, Court Registrar, Drafting Assistant, Compliance Officer, Deadline Tracker)
- What legal domains were touched (DIFC common-law, Dubai Mainland civil-law, arbitration, DIFC Data Protection, UAE Civil Code, corporate, finance, real estate)
- What courts or jurisdictions were referenced (DIFC Courts, Dubai Mainland Courts, DIFC-LCIA, DIAC)
- Any errors or blockers encountered

### Step 2: Run 2-pass leak-check (above)

### Step 3: If passes leak-check, write session summary
Save to `.ailawfirm-dubai/sessions/` with timestamp. Format:
```markdown
# Session — YYYY-MM-DD HH:MM
- Specialists used: [list]
- Domains: [list]
- Courts: [list]
- Key outcomes: [brief]
- Leak-check: PASS (2-pass, Rule 6)
```

### Step 4: Display save confirmation
```
🧠 Dubai-DIFC AI Law Firm — session saved.
   Leak-check: ✅ PASS (Pass 1: 0 AAAK, 0 mempalace | Pass 2: 0 lawtech-arc, 0 personal-build)
   Next session starts smarter.
```

## Output Format
```markdown
## /retrospective — Dubai-DIFC AI Law Firm · Session Save

**Session:** YYYY-MM-DD HH:MM
**Specialists active:** [N]
**Domains touched:** [list]
**Leak-check:** ✅ PASS / ❌ BLOCKED

[If PASS: "Session learning saved. Firm knowledge base updated."]
[If BLOCKED: "Leak detected. Session NOT saved. Review flagged content above."]
```

## Anti-Pollution Rules (DO NOT BREAK)
- Never reference `~/.mempalace/` or any mempalace path
- Never use internal entity codes, matter shorthand, or non-jurisdiction-context identifiers
- Never reference lawtech-arc architecture
- Never reference Wolfgang Rush personal builds or personal brand
- The publisher credit line in README.md is the sole exception — it is public-facing attribution, not a leak

## What this skill does NOT do
- Does NOT read or write to MemPalace
- Does NOT access personal diary, KG, or self-assessment data
- Does NOT touch any other firm's directory
- Does NOT auto-save without passing leak-check
