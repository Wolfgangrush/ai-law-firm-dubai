"""
citation_agent — citation parsing + validation for Dubai-DIFC (v0.1).

Extracts citation strings from natural-language payload, then wraps
dubai_citation_validator MCP tool. Handles DIFC ([2024] DIFC CFI 234)
and Mainland (Arabic case-number) formats.

PROVENANCE: CITED:09-citation-formats.md for citation patterns.
"""

import re
from ailawfirm_dubai.mcp_tools.citation_validator import dubai_citation_validator

_EXTRACTORS = [
    re.compile(r"\[\d{4}\]\s+DIFC\s+(CFI|CA|CASS|SCT)\s+\d+"),
    re.compile(r"Case\s+\d+\s+\d{4}", re.IGNORECASE),
    re.compile(r"قضية\s+\d+\s+\d{4}"),
]


def _extract_citation(text: str) -> str:
    if not text:
        return text
    for pat in _EXTRACTORS:
        m = pat.search(text)
        if m:
            return m.group(0)
    return text.strip()


def handle(payload: str) -> dict:
    cite = _extract_citation(payload)
    result = dubai_citation_validator(cite)
    return {
        "agent": "citation_agent",
        "status": "v0.1 — NL-extracted citation, then validated",
        "extracted": cite,
        "result": result,
    }
