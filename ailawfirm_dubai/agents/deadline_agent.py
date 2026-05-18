"""
deadline_agent — limitation period + deadline check (v0.1 stub).

v0.1: returns known limitation periods from research.
v0.2+: full deadline tracking with calendar integration.

PROVENANCE: CITED:08-limitation-periods-summary.md.
"""

_LIMITATION_PERIODS = {
    "civil": "UAE Civil Code: 15 years general / 3 years commercial (CITED:08-limitation-periods-summary.md)",
    "employment": "DIFC Employment Law: 6 months from termination (CITED:32-difc-employment-law.md)",
    "contract": "DIFC Contract Law: 6 years (CITED:30-contract-law-overview-uae-vs-difc.md)",
    "tort": "UAE Civil Code: 3 years",
    "rental": "Rental disputes: varies by RDC rules (CITED:21-rent-dispute-center-tribunal.md)",
}


def handle(payload: str) -> dict:
    p = payload.lower()
    matches = []
    for key, desc in _LIMITATION_PERIODS.items():
        if key in p:
            matches.append({"type": key, "period": desc})

    return {
        "agent": "deadline_agent",
        "status": "v0.1 — static limitation lookup",
        "matches": matches
        if matches
        else [{"type": "unknown", "period": "specify matter type for limitation check"}],
        "note": "full deadline tracking + calendar integration lands v0.2+",
    }
