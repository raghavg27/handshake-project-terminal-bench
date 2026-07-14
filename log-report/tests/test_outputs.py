import json
from pathlib import Path

REPORT = Path("/app/report.json")


def load_report():
    assert REPORT.exists(), "no report.json at /app/report.json"
    return json.loads(REPORT.read_text())


def test_total_requests():
    """Success criterion 1: total_requests == number of log lines (6)."""
    assert load_report()["total_requests"] == 6


def test_unique_ips():
    """Success criterion 2: unique_ips == distinct client IP count (3)."""
    assert load_report()["unique_ips"] == 3


def test_top_path():
    """Success criterion 3: top_path == most-requested path (/index.html)."""
    assert load_report()["top_path"] == "/index.html"