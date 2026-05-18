"""
dubai_court_lookup MCP tool — v0.1.

Resolves a court name (fuzzy) to structured court info.
v0.1 covers 8 court stubs: 4 DIFC + 4 Mainland.
Each stub has system field (DIFC or MAINLAND) and language_of_proceedings.

PROVENANCE: CITED:01-court-hierarchy.md, 02-difc-court-law.md,
04-dubai-judicial-authority-law.md, 21-rent-dispute-center-tribunal.md.
"""

from typing import Optional
from ailawfirm_dubai.core.ontology import DubaiCourt


_COURT_INFO: dict[DubaiCourt, dict] = {
    # DIFC Courts
    DubaiCourt.DIFC_CFI: {
        "name": "DIFC Court of First Instance",
        "location": "DIFC, Dubai, UAE",
        "tier": "first_instance",
        "system": "DIFC",
        "language_of_proceedings": "en",
        "jurisdiction_class": "original civil + commercial + employment + insolvency",
        "procedural_code": "Rules of the DIFC Courts (RDC)",
        "pecuniary_limit": "Unlimited (CFI); Small Claims Tribunal < USD 500k",
    },
    DubaiCourt.DIFC_CA: {
        "name": "DIFC Court of Appeal",
        "location": "DIFC, Dubai, UAE",
        "tier": "appellate",
        "system": "DIFC",
        "language_of_proceedings": "en",
        "jurisdiction_class": "appeals from DIFC CFI + SCT",
        "procedural_code": "Rules of the DIFC Courts (RDC) Part 44",
        "pecuniary_limit": None,
    },
    DubaiCourt.DIFC_CASSATION: {
        "name": "DIFC Court of Cassation",
        "location": "DIFC, Dubai, UAE",
        "tier": "apex",
        "system": "DIFC",
        "language_of_proceedings": "en",
        "jurisdiction_class": "final appeal on points of law only",
        "procedural_code": "Rules of the DIFC Courts (RDC)",
        "pecuniary_limit": None,
    },
    DubaiCourt.DIFC_SCT: {
        "name": "DIFC Small Claims Tribunal",
        "location": "DIFC, Dubai, UAE",
        "tier": "tribunal",
        "system": "DIFC",
        "language_of_proceedings": "en",
        "jurisdiction_class": "claims < USD 500,000; employment claims (any value)",
        "procedural_code": "RDC Part 53 — Small Claims Tribunal Rules",
        "pecuniary_limit": "USD 500,000",
    },
    # Mainland Courts
    DubaiCourt.DUBAI_CFI: {
        "name": "Dubai Court of First Instance",
        "location": "Dubai, UAE",
        "tier": "first_instance",
        "system": "MAINLAND",
        "language_of_proceedings": "ar",
        "jurisdiction_class": "original civil + criminal + personal status + labour",
        "procedural_code": "UAE Federal Civil Procedure Law",
        "pecuniary_limit": None,
    },
    DubaiCourt.DUBAI_CA: {
        "name": "Dubai Court of Appeal",
        "location": "Dubai, UAE",
        "tier": "appellate",
        "system": "MAINLAND",
        "language_of_proceedings": "ar",
        "jurisdiction_class": "appeals from Dubai CFI",
        "procedural_code": "UAE Federal Civil Procedure Law",
        "pecuniary_limit": None,
    },
    DubaiCourt.DUBAI_CASSATION: {
        "name": "Dubai Court of Cassation",
        "location": "Dubai, UAE",
        "tier": "apex",
        "system": "MAINLAND",
        "language_of_proceedings": "ar",
        "jurisdiction_class": "final appeal on points of law only",
        "procedural_code": "UAE Federal Civil Procedure Law",
        "pecuniary_limit": None,
    },
    DubaiCourt.DUBAI_RDC: {
        "name": "Rental Disputes Center",
        "location": "Dubai, UAE",
        "tier": "tribunal",
        "system": "MAINLAND",
        "language_of_proceedings": "ar",
        "jurisdiction_class": "landlord-tenant disputes · rental matters",
        "procedural_code": "RDC procedural rules (Dubai-specific)",
        "pecuniary_limit": None,
    },
}


def _fuzzy_match_court(query: str) -> Optional[DubaiCourt]:
    """Case-insensitive match on court enum values and names."""
    q = query.lower().strip()
    if not q:
        return None
    q_words = q.split()
    for court in DubaiCourt:
        text = (court.value + " " + court.name).lower()
        if q in text:
            return court
        if q_words and all(w in text for w in q_words):
            return court
    return None


def dubai_court_lookup(court_name: str) -> dict:
    """Resolve a court name (fuzzy) to structured court info.

    Args:
        court_name: free-text court name (e.g. "DIFC Court of Appeal", "Rental Disputes Center",
                    "dubai cfi", "محكمة دبي الابتدائية")

    Returns:
        dict with court info. If no match: {"found": False, "query": <input>}.
    """
    if not isinstance(court_name, str):
        return {"found": False, "error": "court_name must be a string"}

    matched = _fuzzy_match_court(court_name)
    if matched is None or matched not in _COURT_INFO:
        return {"found": False, "query": court_name}

    info = dict(_COURT_INFO[matched])
    info["matched_enum"] = matched.name
    info["found"] = True
    return info
