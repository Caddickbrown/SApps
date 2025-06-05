import os
import sys
import pytest

sys.path.append(os.path.dirname(__file__))
from CounTally import generate_new_count_html, generate_historical_html


def test_generate_new_count_html_contains_tally(tmp_path):
    html = generate_new_count_html(5)
    assert "<span id=\"count\">5</span>" in html


def test_generate_historical_html_contains_rows(tmp_path):
    data = [
        {"Date": "2023-01-01", "Counter Name": "A", "Tally": "2", "Notes": "x"},
        {"Date": "2023-01-02", "Counter Name": "B", "Tally": "3", "Notes": "y"},
    ]
    html = generate_historical_html(data)
    assert "<td>2023-01-01</td>" in html
    assert "<td>A</td>" in html
    assert "<td>3</td>" in html
