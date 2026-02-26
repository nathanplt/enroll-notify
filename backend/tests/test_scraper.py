import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
pytest.importorskip("playwright.async_api")

from app.scraper import status_is_open


@pytest.mark.parametrize(
    "status,expected",
    [
        ("Open 5 of 120", True),
        ("Wait List Open 2 of 30", True),
        ("Wait List Full (30)", True),
        ("Closed Class Full (120)", False),
        ("Closed by Dept Computer Science (0 capacity, 0 enrolled, 0 waitlisted)", False),
        ("   closed class full (120)   ", False),
    ],
)
def test_status_is_open_only_false_for_closed(status: str, expected: bool) -> None:
    assert status_is_open(status) is expected
