from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[2]
PAGE_FILE = REPO_ROOT / "website" / "src" / "pages" / "skills" / "index.tsx"
CSS_FILE = REPO_ROOT / "website" / "src" / "pages" / "skills" / "styles.module.css"


def test_load_more_button_has_full_label_title_preview() -> None:
    page = PAGE_FILE.read_text()

    assert "title={loadMoreLabel}" in page
    assert "const loadMoreLabel = `Show more (${remainingCount} remaining)`;" in page


def test_load_more_button_prevents_wrap_and_truncates() -> None:
    css = CSS_FILE.read_text()

    load_more_block = css.split(".loadMoreBtn {", maxsplit=1)[1].split("}", maxsplit=1)[0]

    assert "white-space: nowrap;" in load_more_block
    assert "overflow: hidden;" in load_more_block
    assert "text-overflow: ellipsis;" in load_more_block
