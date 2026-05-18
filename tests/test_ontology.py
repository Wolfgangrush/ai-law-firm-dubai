"""Tests for Dubai-DIFC ontology module — v0.1."""

from ailawfirm_dubai.core.ontology import (
    System,
    MatterType,
    DubaiCourt,
    DubaiStatute,
    DubaiBarRule,
    Matter,
    Citation,
    CalendarEvent,
)


def test_system_enum_has_three_values():
    assert System.DIFC.value == "DIFC (offshore common-law · English)"
    assert System.MAINLAND.value == "Dubai Mainland (onshore civil-law · Arabic)"
    assert System.BOTH.value == "Dual-system practitioner"


def test_matter_type_has_difc_and_mainland():
    assert MatterType.DIFC_CIVIL.value == "DIFC Civil Claim (CFI)"
    assert MatterType.MAINLAND_CIVIL.value == "Mainland Civil Suit"


def test_matter_type_has_rental():
    assert MatterType.MAINLAND_RENTAL.value == "Rental Disputes Center matter"


def test_court_has_difc_and_mainland():
    assert DubaiCourt.DIFC_CFI.value == "DIFC Court of First Instance"
    assert DubaiCourt.DUBAI_CFI.value == "Dubai Court of First Instance"
    assert DubaiCourt.DUBAI_RDC.value == "Rental Disputes Center"


def test_statute_includes_difc_dpl():
    assert DubaiStatute.DIFC_DPL.value == "DIFC Data Protection Law (No. 5 of 2020) — GDPR-aligned"


def test_statute_includes_uae_aml():
    assert "goAML" in DubaiStatute.UAE_AML.value


def test_bar_rule_clpd():
    assert "16 points" in DubaiBarRule.CLPD_REQUIREMENT.value


def test_no_duplicate_matter_type_values():
    values = [m.value for m in MatterType]
    assert len(values) == len(set(values)), "Duplicate MatterType values"


def test_no_duplicate_court_values():
    values = [c.value for c in DubaiCourt]
    assert len(values) == len(set(values)), "Duplicate DubaiCourt values"


def test_no_duplicate_statute_values():
    values = [s.value for s in DubaiStatute]
    assert len(values) == len(set(values)), "Duplicate DubaiStatute values"


def test_matter_dataclass_dual_system():
    m = Matter(
        matter_id="DIFC-CFI-2026-001",
        matter_type=MatterType.DIFC_CIVIL,
        system=System.DIFC,
        court=DubaiCourt.DIFC_CFI,
        short_title="Acme Corp v. Beta Ltd",
    )
    assert m.matter_id == "DIFC-CFI-2026-001"
    assert m.system == System.DIFC
    assert m.language == "en"
    assert m.parties_plaintiff == []


def test_matter_dataclass_mainland():
    m = Matter(
        matter_id="DXB-CFI-2026-002",
        matter_type=MatterType.MAINLAND_CIVIL,
        system=System.MAINLAND,
        court=DubaiCourt.DUBAI_CFI,
        short_title="Ahmed v. Mohamed",
        language="ar",
    )
    assert m.system == System.MAINLAND
    assert m.language == "ar"


def test_citation_dataclass_difc():
    c = Citation(raw="[2024] DIFC CFI 234", format="DIFC", year=2024, valid=True)
    assert c.format == "DIFC"
    assert c.year == 2024
    assert c.system is None


def test_calendar_event_defaults():
    e = CalendarEvent(uid="test-uid", summary="Hearing", start_time="2026-06-15T10:00:00")
    assert e.timezone == "Asia/Dubai"
    assert e.uid == "test-uid"


def test_calendar_event_matter_link():
    e = CalendarEvent(
        uid="test-uid",
        summary="Hearing",
        start_time="2026-06-15T10:00:00",
        matter_id="DIFC-CFI-2026-001",
    )
    assert e.matter_id == "DIFC-CFI-2026-001"
