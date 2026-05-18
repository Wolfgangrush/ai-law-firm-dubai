"""
Brain classifier — rule-based intent detection for Dubai-DIFC (v0.1).

v0.1 strategy: simple keyword matching. Fast, deterministic, no LLM cost.
v0.2+ upgrade path: replace _RULES with Ollama-based classifier.

11 intents including SYSTEM_SWITCH for mid-session DIFC↔Mainland toggle.

PROVENANCE: TRAINED for keyword set (high-frequency legal terms).
"""

from ailawfirm_dubai.brain.intents import Intent

_RULES: list[tuple[list[str], Intent]] = [
    (
        ["citation", "difc cfi", "difc ca", "difc sct", "cite", "cited", "[20"],
        Intent.CITATION_LOOKUP,
    ),
    (
        [
            "court",
            "jurisdiction",
            "bench",
            "tribunal",
            "difc court",
            "dubai court",
            "rental disputes",
            "court of first instance",
            "court of appeal",
            "cassation",
            " mahkama",
            "محكمة",
        ],
        Intent.COURT_QUERY,
    ),
    (
        [
            "draft",
            "drafting",
            "statement of claim",
            "defence",
            "defense",
            "reply",
            "rejoinder",
            "affidavit",
            "plaint",
            "written statement",
        ],
        Intent.DRAFTING_NEED,
    ),
    (
        [
            "deadline",
            "limitation",
            "due date",
            "hearing date",
            "next date",
            "limitation period",
            "filing deadline",
        ],
        Intent.DEADLINE_CHECK,
    ),
    (
        ["client said", "client called", "client wants", "client emailed", "client confirmed"],
        Intent.CLIENT_COMM,
    ),
    (
        ["calendar", "diary", "schedule", "appointment", "consultation"],
        Intent.CALENDAR_QUERY,
    ),
    (
        ["add to calendar", "schedule hearing", "book", "set reminder"],
        Intent.CALENDAR_ADD,
    ),
    (
        [
            "dpl",
            "difc data",
            "uae dpp",
            "data protection",
            "data breach",
            "goaml",
            "aml",
            "clpd",
            "publicity",
            "solicit",
            "advertis",
            "data subject",
            "kyc",
            "money laundering",
            "license renewal",
            "cpe",
            "conflict of interest",
            "confidential",
        ],
        Intent.COMPLIANCE_FLAG,
    ),
    (
        [
            "switch to difc",
            "switch to mainland",
            "switch system",
            "change system",
            "use difc",
            "use mainland",
        ],
        Intent.SYSTEM_SWITCH,
    ),
    (
        ["matter", "hearing", "filed", "order", "argued", "status", "update"],
        Intent.MATTER_UPDATE,
    ),
]


def classify(text: str) -> Intent:
    """Classify the intent of a user request via keyword match.

    v0.1: rule-based. v0.2+: Ollama-classified.

    Args:
        text: free-text user request

    Returns:
        Intent enum value
    """
    if not isinstance(text, str) or not text.strip():
        return Intent.UNKNOWN

    t = text.lower()
    for keywords, intent in _RULES:
        if any(kw in t for kw in keywords):
            return intent
    return Intent.UNKNOWN
