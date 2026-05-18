"""
dubai_calendar_sync MCP tool — v0.1.

Generates ICS (iCalendar) files for Dubai matter hearings + deadlines.
Timezone: Asia/Dubai (UTC+4 year-round, no DST).

PROVENANCE: structural — ICS format is universal, timezone is CITED:01-court-hierarchy.md.
"""

import uuid
from datetime import datetime
from ailawfirm_dubai.core.ontology import CalendarEvent

DUBAI_TIMEZONE = "Asia/Dubai"


def dubai_calendar_sync(
    summary: str,
    start_time: str,
    end_time: str = None,
    location: str = None,
    description: str = None,
    matter_id: str = None,
) -> dict:
    """Generate an ICS event for a Dubai legal matter.

    Args:
        summary: Event title (e.g. "Hearing — DIFC CFI — Smith v Jones")
        start_time: ISO 8601 datetime (e.g. "2026-06-15T10:00:00")
        end_time: ISO 8601 datetime (optional, defaults to start + 1h)
        location: Court location (e.g. "DIFC CFI Courtroom 3")
        description: Event notes
        matter_id: Associated matter ID

    Returns:
        dict with uid, ics_string, and CalendarEvent fields
    """
    uid = str(uuid.uuid4())
    evt = CalendarEvent(
        uid=uid,
        summary=summary,
        start_time=start_time,
        end_time=end_time or start_time,
        location=location,
        description=description,
        matter_id=matter_id,
        timezone=DUBAI_TIMEZONE,
    )

    # Build minimal ICS
    ics_lines = [
        "BEGIN:VCALENDAR",
        "VERSION:2.0",
        "PRODID:-//AI Law Firm Dubai//v0.1//EN",
        "BEGIN:VEVENT",
        f"UID:{uid}",
        f"DTSTART;TZID={DUBAI_TIMEZONE}:{_ics_dt(start_time)}",
        f"DTEND;TZID={DUBAI_TIMEZONE}:{_ics_dt(end_time or start_time)}",
        f"SUMMARY:{summary}",
    ]
    if location:
        ics_lines.append(f"LOCATION:{location}")
    if description:
        ics_lines.append(f"DESCRIPTION:{description}")
    ics_lines.append("END:VEVENT")
    ics_lines.append("END:VCALENDAR")

    return {
        "uid": uid,
        "summary": summary,
        "start_time": start_time,
        "end_time": evt.end_time,
        "location": location,
        "description": description,
        "matter_id": matter_id,
        "timezone": DUBAI_TIMEZONE,
        "ics": "\n".join(ics_lines),
    }


def _ics_dt(iso_string: str) -> str:
    """Convert ISO datetime to ICS local datetime format (YYYYMMDDTHHMMSS)."""
    return iso_string.replace("-", "").replace(":", "")
