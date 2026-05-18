"""Tests for dubai_citation_validator MCP tool — v0.1."""

from ailawfirm_dubai.mcp_tools.citation_validator import dubai_citation_validator


# DIFC tests
def test_difc_cfi_valid():
    r = dubai_citation_validator("[2024] DIFC CFI 234")
    assert r["valid"] is True
    assert r["format"] == "DIFC"
    assert r["year"] == 2024
    assert r["court_or_reporter"] == "DIFC CFI"
    assert r["case_number"] == 234
    assert r["system"] == "DIFC"


def test_difc_ca_valid():
    r = dubai_citation_validator("[2023] DIFC CA 56")
    assert r["valid"] is True
    assert r["format"] == "DIFC"
    assert r["year"] == 2023
    assert r["court_or_reporter"] == "DIFC CA"


def test_difc_sct_valid():
    r = dubai_citation_validator("[2025] DIFC SCT 1024")
    assert r["valid"] is True
    assert r["format"] == "DIFC"
    assert r["court_or_reporter"] == "DIFC SCT"


def test_difc_cassation_valid():
    r = dubai_citation_validator("[2024] DIFC CASS 15")
    assert r["valid"] is True
    assert r["court_or_reporter"] == "DIFC CASS"


# Mainland tests
def test_mainland_case_english_valid():
    r = dubai_citation_validator("Case 456 2023 (Dubai CFI)")
    assert r["valid"] is True
    assert r["format"] == "MAINLAND"
    assert r["year"] == 2023
    assert r["case_number"] == 456
    assert r["system"] == "MAINLAND"


def test_mainland_case_arabic_valid():
    r = dubai_citation_validator("قضية 789 2024")
    assert r["valid"] is True
    assert r["format"] == "MAINLAND"
    assert r["year"] == 2024


# Invalid / unknown
def test_difc_invalid_format():
    r = dubai_citation_validator("[2024] DIFC XYZ 234")
    assert r["valid"] is False


def test_unknown_format():
    r = dubai_citation_validator("Foo Bar 2023 Baz")
    assert r["valid"] is False
    assert r["format"] == "UNKNOWN"


def test_empty_string():
    r = dubai_citation_validator("")
    assert r["valid"] is False


def test_non_string_input():
    r = dubai_citation_validator(12345)
    assert r["valid"] is False
    assert "not a string" in r["parse_notes"]
