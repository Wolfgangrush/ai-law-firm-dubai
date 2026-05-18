"""Tests for dubai_calendar_sync MCP tool — v0.1."""

from ailawfirm_dubai.mcp_tools.calendar_sync import dubai_calendar_sync, DUBAI_TIMEZONE


def test_calendar_sync_basic():
    r = dubai_calendar_sync(
        summary="Hearing — DIFC CFI — Acme v Beta",
        start_time="2026-06-15T10:00:00",
    )
    assert r["uid"] is not None
    assert r["summary"] == "Hearing — DIFC CFI — Acme v Beta"
    assert r["timezone"] == "Asia/Dubai"
    assert r["ics"].startswith("BEGIN:VCALENDAR")
    assert "END:VCALENDAR" in r["ics"]


def test_calendar_sync_with_location():
    r = dubai_calendar_sync(
        summary="Case Management Conference",
        start_time="2026-07-01T09:00:00",
        location="DIFC CFI Courtroom 3",
    )
    assert r["location"] == "DIFC CFI Courtroom 3"
    assert "LOCATION:DIFC CFI Courtroom 3" in r["ics"]


def test_calendar_sync_with_matter_id():
    r = dubai_calendar_sync(
        summary="Hearing",
        start_time="2026-08-01T11:00:00",
        matter_id="DIFC-CFI-2026-001",
    )
    assert r["matter_id"] == "DIFC-CFI-2026-001"


def test_calendar_sync_tz_always_asia_dubai():
    r = dubai_calendar_sync(
        summary="RDC Mediation",
        start_time="2026-09-01T14:00:00",
    )
    assert r["timezone"] == DUBAI_TIMEZONE
    assert "TZID=Asia/Dubai" in r["ics"]
