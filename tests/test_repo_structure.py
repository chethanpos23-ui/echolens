"""Structure and documentation tests for EchoLens.

These run in CI. They do not test application behaviour — they assert that the repository
keeps the shape its documentation promises, which is the failure mode a case-study repository
actually has.
"""
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".gitignore",
    ".github/PULL_REQUEST_TEMPLATE.md",
    ".github/ISSUE_TEMPLATE/bug_report.md",
    ".github/ISSUE_TEMPLATE/feature_request.md",
    ".github/workflows/ci.yml",
    "docs/architecture.md",
    "evaluation/description-quality.md",
    "evaluation/latency-results.csv",
]

REQUIRED_DIRS = [
    "mobile",
    "server",
    "models",
    "accessibility-tests",
    "demo",
]

REQUIRED_README_SECTIONS = [
    "The Problem",
    "Our Solution",
    "Demo",
    "Features",
    "Architecture",
    "Technology",
    "My Contribution",
    "Local Setup",
    "Testing",
    "Limitations",
    "Responsible Use",
    "Future Improvements",
    "Team",
    "License",
]


def _read(rel):
    with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
        return f.read()


def test_required_files_exist():
    missing = [p for p in REQUIRED_FILES if not os.path.isfile(os.path.join(ROOT, p))]
    assert not missing, f"missing required files: {missing}"


def test_required_directories_exist():
    missing = [d for d in REQUIRED_DIRS if not os.path.isdir(os.path.join(ROOT, d))]
    assert not missing, f"missing required directories: {missing}"


def test_readme_has_every_template_section():
    headings = set(re.findall(r"^##\s+(.+)$", _read("README.md"), flags=re.M))
    missing = [s for s in REQUIRED_README_SECTIONS if s not in headings]
    assert not missing, f"README is missing sections: {missing}"


def test_readme_states_the_project_is_a_case_study():
    readme = _read("README.md").lower()
    assert "case study" in readme, "README must state that this is a portfolio case study"


def test_readme_limitations_are_not_empty():
    readme = _read("README.md")
    section = readme.split("## Limitations", 1)[1].split("##", 1)[0]
    bullets = [ln for ln in section.splitlines() if ln.strip().startswith("-")]
    assert len(bullets) >= 3, "Limitations should list at least three honest constraints"


def test_no_placeholder_markers_left_in_docs():
    offenders = []
    for dirpath, dirnames, filenames in os.walk(ROOT):
        dirnames[:] = [d for d in dirnames if d not in {".git", "node_modules", ".github"}]
        for name in filenames:
            if not name.endswith(".md"):
                continue
            path = os.path.join(dirpath, name)
            with open(path, encoding="utf-8") as f:
                text = f.read()
            if "PROJECT_SLUG" in text or "LOREM IPSUM" in text.upper():
                offenders.append(os.path.relpath(path, ROOT))
    assert not offenders, f"placeholder markers left in: {offenders}"


def test_license_names_an_author():
    assert "Chethan Posani" in _read("LICENSE")
