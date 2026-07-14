from pathlib import Path

from app.agent import (
    create_implementation_plan,
    discover_context_files,
    extract_keywords,
)


def test_extract_keywords_removes_common_words() -> None:
    keywords = extract_keywords(
        "Add CSV export",
        "Users need to export filtered reports as CSV.",
    )

    assert "csv" in keywords
    assert "export" in keywords
    assert "users" not in keywords


def test_discover_context_files(tmp_path: Path) -> None:
    (tmp_path / "csv_export.py").write_text("def export_csv(): pass")
    (tmp_path / "unrelated.txt").write_text("ignore")

    matches = discover_context_files(str(tmp_path), ["csv", "export"])

    assert matches == ["csv_export.py"]


def test_plan_contains_testing_step() -> None:
    plan = create_implementation_plan(
        "Add CSV export",
        ["csv", "export"],
        ["reports.py"],
    )

    assert any("test" in step.lower() for step in plan)
