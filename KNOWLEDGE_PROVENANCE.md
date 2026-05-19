# KNOWLEDGE_PROVENANCE — AI Law Firm · Dubai-DIFC · Solo · v0.1

Maps every domain claim in the codebase to its source. Prevents silent introduction of hallucinated legal facts.

## Provenance categories

- **TRAINED** — model's training corpus. Reliable for high-frequency facts (e.g. "DIFC Courts exist"); UNRELIABLE for recent statutes, amendments, specific judge dispositions.
- **CITED** — backed by a specific source in `_research/` that the verifier can inspect.
- **STUB** — placeholder for v0.2+ where real content lands.

## DIFC Courts (CITED: _research/01-court-hierarchy.md + 02-difc-court-law.md)

| Claim | Provenance |
|---|---|
| DIFC Court of First Instance (CFI) exists | CITED:01-court-hierarchy.md |
| DIFC Court of Appeal (CA) exists | CITED:01-court-hierarchy.md |
| DIFC Court of Cassation exists | CITED:02-difc-court-law.md |
| DIFC Small Claims Tribunal (SCT) exists | CITED:03-difc-court-rules-rdc.md |
| DIFC Wills and Probate Registry exists | CITED:02-difc-court-law.md |
| DIFC Courts use English language of proceedings | CITED:01-court-hierarchy.md |

## Mainland Courts (CITED: _research/01-court-hierarchy.md + 04-dubai-judicial-authority-law.md)

| Claim | Provenance |
|---|---|
| Dubai Court of First Instance exists | CITED:01-court-hierarchy.md |
| Dubai Court of Appeal exists | CITED:01-court-hierarchy.md |
| Dubai Court of Cassation exists | CITED:01-court-hierarchy.md |
| Rental Disputes Center (RDC) exists | CITED:21-rent-dispute-center-tribunal.md |
| Mainland courts use Arabic language of proceedings | CITED:04-dubai-judicial-authority-law.md |

## DIFC Statutes (CITED: respective _research files)

| Statute | Provenance |
|---|---|
| DIFC Contract Law (Amendment No. 5 of 2024) | CITED:30-contract-law-overview-uae-vs-difc.md |
| DIFC Employment Law (No. 2 of 2019) | CITED:32-difc-employment-law.md |
| DIFC Data Protection Law (No. 5 of 2020) | CITED:13-difc-data-protection-law.md |
| DIFC Companies Law | CITED:33-uae-commercial-companies-law.md |
| DIFC Insolvency Law | CITED:34-difc-insolvency-law.md |
| Rules of the DIFC Courts (RDC) | CITED:03-difc-court-rules-rdc.md |
| DIFC Arbitration Law (No. 1 of 2008) | CITED:_statute_corpus/arbitration_law_2008.md |
| DIFC Trust Law (No. 4 of 2018) | CITED:_statute_corpus/trust_law_2018.md |
| DIFC Real Property Law (No. 1 of 2018) | CITED:_statute_corpus/property_law_2018.md |
| DIFC Personal Property Law (No. 9 of 2005) | CITED:_statute_corpus/personal_property_law_2005.md |
| DIFC Court Law (No. 10 of 2004, consolidated Dubai Law No. 2 of 2025) | CITED:_statute_corpus/court_law_2004.md |
| DIFC Law of Obligations (No. 5 of 2005) | CITED:_statute_corpus/obligations_law_2005.md |
| DIFC Digital Assets Law (No. 2 of 2024) | CITED:_statute_corpus/digital_assets_law_2024.md |
| DIFC Regulatory Law (No. 1 of 2004) | CITED:_statute_corpus/regulatory_law_2004.md |
| Decree 19/2016 — Decree 29/2024 (DIFC-Mainland conflicts) | CITED:_statute_corpus/conflicts_decree_19_29.md |

## UAE Federal Statutes (Mainland-applicable)

| Statute | Provenance |
|---|---|
| UAE Federal Civil Transactions Law (Civil Code) | CITED:05-uae-civil-transactions-law.md |
| UAE Federal Commercial Transactions Law | CITED:05-uae-civil-transactions-law.md |
| UAE Federal Penal Code | TRAINED |
| UAE Federal Personal Status Law | TRAINED |
| Federal DPP (Decree-Law No. 45 of 2021) | CITED:14-uae-personal-data-protection-law.md |
| AML (Decree-Law No. 20 of 2018) — goAML mandatory | CITED:24-anti-money-laundering-aml-uae.md |

## Bar Rules & Professional Regulation

| Rule | Provenance |
|---|---|
| UAE Federal Law on the Legal Profession (Mainland advocates) | CITED:06-uae-legal-profession-law.md |
| Dubai Legal Profession Regulation | CITED:07-dubai-legal-profession-regulation.md |
| DIFC Academy of Law Code of Conduct | CITED:10-bar-rule-publicity-solicitation.md |
| CLPD: 16 points/year mandatory for license renewal | CITED:26-mandatory-cpe-clpd-requirements.md |
| Publicity/solicitation restrictions | CITED:10-bar-rule-publicity-solicitation.md |
| Conflict of interest rules | CITED:11-bar-rule-conflict-of-interest.md |
| Confidentiality obligations | CITED:12-bar-rule-confidentiality.md |

## Citation Formats (CITED: _research/09-citation-formats.md)

| Format | Provenance |
|---|---|
| DIFC: `[YYYY] DIFC CFI Number` | CITED:09-citation-formats.md |
| DIFC: `[YYYY] DIFC CA Number` | CITED:09-citation-formats.md |
| DIFC: `[YYYY] DIFC SCT Number` | CITED:09-citation-formats.md |
| Mainland: Arabic case-number format | CITED:09-citation-formats.md |

## Key Practical Facts

| Fact | Provenance |
|---|---|
| E-filing system: Salif/CMS | CITED:16-e-filing-system-salif-cms.md |
| Digital identity: UAE PASS | CITED:16-e-filing-system-salif-cms.md |
| Cause-list system: Dubai-DIFC | CITED:15-cause-list-system-dubai-difc.md |
| Arbitration: DIAC framework | CITED:22-arbitration-diac-framework.md |
| AI legal tech UAE strategy | CITED:23-ai-legal-tech-uae-strategy.md |
| Evidence law: UAE Federal | CITED:28-evidence-law-federal-uae.md |
| Cybersecurity obligations for lawyers | CITED:29-cybersecurity-obligations-for-lawyers.md |
| Limitation periods | CITED:08-limitation-periods-summary.md |
| Firm structure: sole prop / civil company | CITED:25-firm-structure-options-sole-prop-civil.md |
| Licensing pathway: expats vs locals | CITED:27-licensing-pathway-for-expats-vs-locals.md |
| Solo advocate economic reality | CITED:19-solo-advocate-economic-reality.md |
| Solo advocate pain points | CITED:20-solo-advocate-pain-points.md |
| Legal aid system: Dubai Courts | CITED:17-legal-aid-system-dubai-courts.md |

## Verification protocol

Before any v0.1 → v0.2 transition, the publisher reviews this file. Items in `_research/` are the authoritative source for v0.1 claims.

## What this file is NOT

- Not a comprehensive legal database.
- Not a substitute for a lawyer's own statutory research.
- Not a fixed document — every change in domain content must update this file in the same commit.
