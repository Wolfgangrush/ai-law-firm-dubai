"""Tests for Dubai-DIFC brain classifier — v0.1."""

from ailawfirm_dubai.brain.classifier import classify
from ailawfirm_dubai.brain.intents import Intent


def test_classify_system_switch_to_difc():
    assert classify("switch to DIFC") == Intent.SYSTEM_SWITCH


def test_classify_system_switch_to_mainland():
    assert classify("switch to mainland please") == Intent.SYSTEM_SWITCH


def test_classify_citation_lookup():
    assert classify("validate [2024] DIFC CFI 234") == Intent.CITATION_LOOKUP


def test_classify_court_query():
    assert classify("tell me about DIFC Court of Appeal") == Intent.COURT_QUERY


def test_classify_compliance_flag_goaml():
    assert classify("do I need to file goAML for this") == Intent.COMPLIANCE_FLAG


def test_classify_compliance_flag_dpl():
    assert classify("DIFC data protection compliance check") == Intent.COMPLIANCE_FLAG


def test_classify_compliance_flag_clpd():
    assert classify("CLPD license renewal requirements") == Intent.COMPLIANCE_FLAG


def test_classify_calendar_query():
    assert classify("check my calendar for next week") == Intent.CALENDAR_QUERY


def test_classify_drafting():
    assert classify("I need to draft a statement of claim") == Intent.DRAFTING_NEED


def test_classify_deadline():
    assert classify("what is the limitation period for civil claims") == Intent.DEADLINE_CHECK


def test_classify_unknown():
    assert classify("hello how are you") == Intent.UNKNOWN


def test_classify_empty_string():
    assert classify("") == Intent.UNKNOWN


def test_classify_non_string():
    assert classify(None) == Intent.UNKNOWN
