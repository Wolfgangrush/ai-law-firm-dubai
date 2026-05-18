"""
dubai_citation_validator MCP tool — v0.1.

Validates and parses Dubai legal citations against dual-system formats:
- DIFC: [YYYY] DIFC CFI/CA/CASS/SCT Number (e.g. [2024] DIFC CFI 234)
- Mainland: Case/قضية Number Year (Court) (variable format)

v0.1: format validation + parsing only. v0.3+ adds database lookup.

PROVENANCE: CITED:09-citation-formats.md for citation patterns.
"""

import re


_DIFC_PATTERN = re.compile(
    r"^\[(?P<year>\d{4})\]\s+DIFC\s+(?P<court>CFI|CA|CASS|SCT)\s+(?P<num>\d+)$"
)
_MAINLAND_PATTERN = re.compile(
    r"^(?P<case_type>Case|قضية)\s+(?P<num>\d+)\s+(?P<year>\d{4})(\s+\((?P<court>.+?)\))?$",
    re.IGNORECASE,
)


def dubai_citation_validator(citation_string: str) -> dict:
    """Parse and validate a Dubai legal citation.

    Args:
        citation_string: e.g. "[2024] DIFC CFI 234" or "Case 456 2023 (Dubai CFI)"

    Returns:
        dict with: raw, format ('DIFC'|'MAINLAND'|'UNKNOWN'), year, court_or_reporter,
        case_number, valid, parse_notes, system
    """
    if not isinstance(citation_string, str):
        return {
            "raw": str(citation_string),
            "format": "UNKNOWN",
            "valid": False,
            "parse_notes": "input was not a string",
            "system": None,
        }

    s = citation_string.strip()

    # Try DIFC
    m = _DIFC_PATTERN.match(s)
    if m:
        return {
            "raw": s,
            "format": "DIFC",
            "year": int(m.group("year")),
            "court_or_reporter": f"DIFC {m.group('court')}",
            "case_number": int(m.group("num")),
            "valid": True,
            "parse_notes": None,
            "system": "DIFC",
        }

    # Try Mainland
    m = _MAINLAND_PATTERN.match(s)
    if m:
        return {
            "raw": s,
            "format": "MAINLAND",
            "year": int(m.group("year")),
            "court_or_reporter": m.group("court") or "Dubai Courts",
            "case_number": int(m.group("num")),
            "valid": True,
            "parse_notes": None,
            "system": "MAINLAND",
        }

    return {
        "raw": s,
        "format": "UNKNOWN",
        "year": None,
        "court_or_reporter": None,
        "case_number": None,
        "valid": False,
        "parse_notes": "did not match DIFC or Mainland citation patterns",
        "system": None,
    }
