import sys
from cli import parse_args


def test_parse_args(monkeypatch):
    monkeypatch.setattr(
        sys,
        "argv",
        ["main.py", "--files", "a.csv", "--report", "median-coffee"]
    )

    args = parse_args()

    assert args.report == "median-coffee"
    assert args.files == ["a.csv"]