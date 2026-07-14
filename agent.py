from __future__ import annotations

from pathlib import Path
import re

STOP_WORDS = {
    "a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in",
    "is", "it", "of", "on", "or", "that", "the", "this", "to", "users", "with"
}

ALLOWED_EXTENSIONS = {
    ".py", ".js", ".jsx", ".ts", ".tsx", ".java", ".go", ".rs",
    ".md", ".json", ".yml", ".yaml", ".toml", ".sql"
}


def extract_keywords(title: str, body: str, limit: int = 8) -> list[str]:
    words = re.findall(r"[A-Za-z][A-Za-z0-9_-]{2,}", f"{title} {body}".lower())
    unique: list[str] = []

    for word in words:
        if word not in STOP_WORDS and word not in unique:
            unique.append(word)

    return unique[:limit]


def discover_context_files(
    repository_path: str,
    keywords: list[str],
    limit: int = 10,
) -> list[str]:
    root = Path(repository_path).expanduser().resolve()

    if not root.exists() or not root.is_dir():
        return []

    scored: list[tuple[int, str]] = []

    for path in root.rglob("*"):
        if not path.is_file() or path.suffix.lower() not in ALLOWED_EXTENSIONS:
            continue

        relative = str(path.relative_to(root))
        lowered = relative.lower()
        score = sum(1 for keyword in keywords if keyword in lowered)

        if score:
            scored.append((score, relative))

    scored.sort(key=lambda item: (-item[0], item[1]))
    return [path for _, path in scored[:limit]]


def create_implementation_plan(
    title: str,
    keywords: list[str],
    context_files: list[str],
) -> list[str]:
    context_step = (
        f"Review the most relevant files: {', '.join(context_files[:5])}."
        if context_files
        else "Identify the modules and tests affected by the requested change."
    )

    focus = ", ".join(keywords[:5]) if keywords else "the requested behaviour"

    return [
        f"Clarify the acceptance criteria for: {title}.",
        context_step,
        f"Design the smallest maintainable change focused on {focus}.",
        "Implement the change with input validation and clear error handling.",
        "Add or update automated tests for expected, edge, and failure cases.",
        "Run the complete test suite and document any known limitations.",
    ]


def create_pull_request_summary(
    title: str,
    plan: list[str],
    context_files: list[str],
) -> str:
    files_text = (
        ", ".join(context_files[:5])
        if context_files
        else "Relevant files will be confirmed during implementation"
    )

    return (
        f"## Summary\n"
        f"Proposes an implementation plan for **{title}**.\n\n"
        f"## Likely areas\n{files_text}\n\n"
        f"## Validation\n"
        f"- Add targeted automated tests\n"
        f"- Run the full test suite\n"
        f"- Review error handling and backward compatibility\n\n"
        f"## Planned steps\n"
        + "\n".join(f"- {step}" for step in plan)
    )
