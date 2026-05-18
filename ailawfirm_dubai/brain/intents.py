"""
Intent enum for the AI Law Firm Dubai-DIFC brain layer.

The brain classifies incoming user requests into one of these intents,
then routes to the matching agent. 11 intents including SYSTEM_SWITCH
for DIFC↔Mainland toggle.

PROVENANCE: STUB — v0.2+ will add Ollama-based classification.
v0.1 uses rule-based keyword matching (see classifier.py).
"""

from enum import Enum


class Intent(Enum):
    """User request intents for Dubai-DIFC legal practice."""

    MATTER_UPDATE = "matter_update"
    CITATION_LOOKUP = "citation_lookup"
    COURT_QUERY = "court_query"
    DRAFTING_NEED = "drafting_need"
    DEADLINE_CHECK = "deadline_check"
    CLIENT_COMM = "client_comm"
    COMPLIANCE_FLAG = "compliance_flag"
    CALENDAR_QUERY = "calendar_query"
    CALENDAR_ADD = "calendar_add"
    SYSTEM_SWITCH = "system_switch"
    UNKNOWN = "unknown"


AGENT_FOR_INTENT: dict[Intent, str] = {
    Intent.MATTER_UPDATE: "matter_agent",
    Intent.CITATION_LOOKUP: "citation_agent",
    Intent.COURT_QUERY: "court_agent",
    Intent.DRAFTING_NEED: "drafting_agent",
    Intent.DEADLINE_CHECK: "deadline_agent",
    Intent.CLIENT_COMM: "matter_agent",
    Intent.COMPLIANCE_FLAG: "compliance_agent",
    Intent.CALENDAR_QUERY: "matter_agent",
    Intent.CALENDAR_ADD: "matter_agent",
    Intent.SYSTEM_SWITCH: "system_switch_agent",
    Intent.UNKNOWN: "matter_agent",
}
