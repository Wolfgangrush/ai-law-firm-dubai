# Statute Corpus Summary — Dubai-DIFC

## Date: 2026-05-19
## Total DIFC statutes digested: 15
## Mainland UAE statutes digested: 0 (Mainland coverage shipped via drafting templates + system_switch_agent, with full Federal-law text deferred to v0.2)
## STATUS: v0.1 ship-ready

## DIFC statute coverage (15 files)

| Slug | Statute | Citation | Status |
|---|---|---|---|
| arbitration_law_2008 | DIFC Arbitration Law | DIFC Law No 1 of 2008 (UNCITRAL Model Law basis) | v0.1 digested |
| companies_law_2018 | DIFC Companies Law | DIFC Law No 5 of 2018 (repeals Companies Law 2009) | v0.1 digested |
| conflicts_decree_19_29 | DIFC-Mainland Conflicts | Decree No 19 of 2016 / Decree No 29 of 2024 (Judicial Authority) | v0.1 digested |
| contract_law_2004 | DIFC Contract Law | DIFC Law No 6 of 2004 | v0.1 digested |
| court_law_2004 | DIFC Court Law | DIFC Law No 10 of 2004 / Dubai Law No 2 of 2025 | v0.1 digested |
| data_protection_law_2020 | DIFC Data Protection Law | DIFC Law No 5 of 2020 (GDPR-aligned) | v0.1 digested |
| digital_assets_law_2024 | DIFC Digital Assets Law | DIFC Law No 2 of 2024 | v0.1 digested |
| employment_law_2019 | DIFC Employment Law | DIFC Law No 2 of 2019 (note: 2021 update is v0.2) | v0.1 digested |
| insolvency_law_2019 | DIFC Insolvency Law | DIFC Law No 1 of 2019 (UNCITRAL Model Law cross-border) | v0.1 digested |
| obligations_law_2005 | DIFC Law of Obligations | DIFC Law No 5 of 2005 | v0.1 digested |
| personal_property_law_2005 | DIFC Personal Property Law | DIFC Law No 9 of 2005 | v0.1 digested |
| property_law_2018 | DIFC Real Property Law | DIFC Law No 1 of 2018 | v0.1 digested |
| rdc_rules_summary | DIFC Rules of Court | RDC (Rules of the DIFC Courts) | v0.1 digested |
| regulatory_law_2004 | DIFC Regulatory Law | DIFC Law No 1 of 2004 (establishes DFSA + FMT) | v0.1 digested |
| trust_law_2018 | DIFC Trust Law | DIFC Law No 4 of 2018 | v0.1 digested |

## Mainland UAE coverage approach
Mainland UAE federal-law substantive content is delivered via:
- Drafting templates in `_drafting_data/` (Mainland-tagged variants for contracts, pleadings, applications)
- `ailawfirm_dubai.agents.system_switch_agent` (DIFC ↔ Mainland routing)
- v0.2 will add Federal statute-text digests (Civil Code 1985, Commercial Transactions 2022, Penal 2021, PDPL 2021, Labour 2021, CPL 2022, Companies 2021)

## Authoritative sources used
- difc.ae/business/laws-and-regulations
- DIFC Courts Judgments Portal

## Currency warnings
- DIFC Employment Law 2019: 2021 update (DIFC Law No 4 of 2021) in v0.2 scope
- DIFC Data Protection Law 2020: monitor Executive Regulation updates
- Decree 19/2016 superseded by Decree 29/2024: verify currency at each user query
- DIFC Digital Assets Law 2024: monitor Cabinet Resolution amendments
- DIFC Court Law: Dubai Law No 2 of 2025 consolidation — monitor further amendments

## Cross-references
- Ontology: `ailawfirm_dubai/core/ontology.py` references all 15 statutes
- Provenance: `KNOWLEDGE_PROVENANCE.md` cites all 15 statute files
- Drafting templates: `_drafting_data/` covers DIFC + Mainland for contracts, pleadings, applications

## Recommended next pass (v0.2)
1. Update DIFC Employment Law 2019 → 2021 (DIFC Law No 4 of 2021)
2. Add Mainland UAE Federal statute-text digests (7 Tier 1 statutes)
3. Add DIFC LCIA + DIAC arbitration rules digests
4. Expand Decree 19/2016 → Decree 29/2024 cross-system rules to procedural depth
5. Add DIFC Law of Security 2024 (collateral over personal property — cross-referenced from Personal Property Law)
