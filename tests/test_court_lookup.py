"""Tests for dubai_court_lookup MCP tool — v0.1."""

from ailawfirm_dubai.mcp_tools.court_lookup import dubai_court_lookup


def test_lookup_difc_cfi_exact():
    r = dubai_court_lookup("DIFC Court of First Instance")
    assert r["found"] is True
    assert r["system"] == "DIFC"
    assert r["language_of_proceedings"] == "en"


def test_lookup_difc_sct_fuzzy():
    r = dubai_court_lookup("Small Claims Tribunal")
    assert r["found"] is True
    assert r["matched_enum"] == "DIFC_SCT"
    assert r["pecuniary_limit"] == "USD 500,000"


def test_lookup_dubai_cfi_fuzzy():
    r = dubai_court_lookup("dubai court of first instance")
    assert r["found"] is True
    assert r["system"] == "MAINLAND"
    assert r["language_of_proceedings"] == "ar"


def test_lookup_rental_disputes():
    r = dubai_court_lookup("Rental Disputes Center")
    assert r["found"] is True
    assert r["matched_enum"] == "DUBAI_RDC"
    assert r["system"] == "MAINLAND"


def test_lookup_difc_cassation():
    r = dubai_court_lookup("DIFC Court of Cassation")
    assert r["found"] is True
    assert r["tier"] == "apex"


def test_lookup_unknown_returns_not_found():
    r = dubai_court_lookup("Mars Family Court")
    assert r["found"] is False
    assert r["query"] == "Mars Family Court"


def test_lookup_empty_string():
    r = dubai_court_lookup("")
    assert r["found"] is False


def test_lookup_non_string_input():
    r = dubai_court_lookup(12345)
    assert r["found"] is False
    assert "error" in r
