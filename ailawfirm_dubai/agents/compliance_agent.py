"""
compliance_agent — Dubai-DIFC dual-system compliance firewall (v0.1).

Detects compliance keywords and returns structured flags for:
- DIFC Data Protection Law (No. 5 of 2020) — GDPR-aligned
- UAE Federal DPP (Decree-Law No. 45 of 2021)
- UAE AML (Decree-Law No. 20 of 2018) — goAML mandatory
- CLPD — 16 points/year mandatory
- Publicity/solicitation restrictions
- Conflict of interest + confidentiality rules

PROVENANCE: CITED:13-difc-data-protection-law.md, 14-uae-personal-data-protection-law.md,
24-anti-money-laundering-aml-uae.md, 10-bar-rule-publicity-solicitation.md,
26-mandatory-cpe-clpd-requirements.md.
"""

from ailawfirm_dubai.core.ontology import DubaiBarRule


def handle(payload: str) -> dict:
    p = payload.lower()
    flags = []

    if any(k in p for k in ["dpl", "difc data", "data subject", "dp law"]):
        flags.append(
            {
                "rule": "DIFC Data Protection Law (No. 5 of 2020) — GDPR-aligned",
                "research_ref": "13-difc-data-protection-law.md",
            }
        )

    if any(k in p for k in ["uae dpp", "federal data", "uae personal data"]):
        flags.append(
            {
                "rule": "UAE Federal Decree-Law No. 45 of 2021 — Personal Data Protection",
                "research_ref": "14-uae-personal-data-protection-law.md",
            }
        )

    if any(k in p for k in ["goaml", "aml", "money laundering", "kyc"]):
        flags.append(
            {
                "rule": "UAE Federal AML Law + goAML mandatory reporting",
                "research_ref": "24-anti-money-laundering-aml-uae.md",
            }
        )

    if any(k in p for k in ["clpd", "license renewal", "cpe"]):
        flags.append(
            {
                "rule": DubaiBarRule.CLPD_REQUIREMENT.value,
                "research_ref": "26-mandatory-cpe-clpd-requirements.md",
            }
        )

    if any(k in p for k in ["publicity", "solicit", "advertis", "touting"]):
        flags.append(
            {
                "rule": DubaiBarRule.PUBLICITY_RESTRICTION.value,
                "research_ref": "10-bar-rule-publicity-solicitation.md",
            }
        )

    if any(k in p for k in ["conflict of interest", "conflicting"]):
        flags.append(
            {
                "rule": DubaiBarRule.CONFLICT_OF_INTEREST.value,
                "research_ref": "11-bar-rule-conflict-of-interest.md",
            }
        )

    if any(k in p for k in ["confidential", "privilege"]):
        flags.append(
            {
                "rule": DubaiBarRule.CONFIDENTIALITY.value,
                "research_ref": "12-bar-rule-confidentiality.md",
            }
        )

    return {
        "agent": "compliance_agent",
        "status": "v0.1 — Dubai dual-system firewall",
        "flags": flags,
        "note": "full compliance pipeline lands v0.2+",
    }
