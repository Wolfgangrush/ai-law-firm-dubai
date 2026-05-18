"""
court_agent — court info + jurisdiction lookup for Dubai-DIFC (v0.1).

Strips natural-language preamble ("tell me about", "what is", etc.)
from payload before passing to dubai_court_lookup. Handles both
DIFC courts (English) and Mainland courts (Arabic/English).

PROVENANCE: CITED:01-court-hierarchy.md.
"""

import re
from ailawfirm_dubai.mcp_tools.court_lookup import dubai_court_lookup

_PREAMBLE_RE = re.compile(
    r"^(tell me about|what is|what's|describe|info on|info about|details on|details about|"
    r"show me|lookup|look up|find|locate|please)\s+(the\s+)?",
    re.IGNORECASE,
)
_TRAILING_RE = re.compile(r"\s*(please|kindly|thanks|thank you)\s*[.?!]*\s*$", re.IGNORECASE)


def _strip_preamble(text: str) -> str:
    if not text:
        return text
    cleaned = _PREAMBLE_RE.sub("", text.strip())
    cleaned = _TRAILING_RE.sub("", cleaned)
    return cleaned.strip().rstrip("?.!")


def handle(payload: str) -> dict:
    cleaned = _strip_preamble(payload)
    result = dubai_court_lookup(cleaned)
    return {
        "agent": "court_agent",
        "status": "v0.1 — preamble-stripped lookup",
        "extracted": cleaned,
        "result": result,
    }
