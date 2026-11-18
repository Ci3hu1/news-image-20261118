"""Tests for the news-image-20261118 entry.

Run: python3 -m pytest tests/  (or python3 tests/test_entry.py)
Pure stdlib + PIL for the dimension check; no network.
"""
import hashlib
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))

REPO = Path(__file__).resolve().parent.parent
IMAGE = REPO / "news.png"
EXPECTED_DIGEST = (
    "c26a547e0eff571bcf86ad48616e96dcffae7b70247cc19ce4a66925aa6f8edc"
)


def _run_main(out: Path) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(REPO / "main.py"), "--output", str(out)],
        capture_output=True, text=True, cwd=REPO,
    )


def test_image_exists_and_matches_digest():
    assert IMAGE.is_file(), "news.png missing"
    digest = hashlib.sha256(IMAGE.read_bytes()).hexdigest()
    assert digest == EXPECTED_DIGEST, f"digest mismatch: {digest}"
    assert IMAGE.stat().st_size <= 1_048_576, "image over 1 MiB cap"


def test_image_dimensions():
    from PIL import Image

    with Image.open(IMAGE) as im:
        assert im.size[0] <= 1024 and im.size[1] <= 1024, im.size
        assert im.size == (1024, 1024), im.size


def test_deterministic_two_runs():
    with tempfile.TemporaryDirectory() as td:
        out1 = Path(td) / "one.png"
        out2 = Path(td) / "two.png"
        r1 = _run_main(out1)
        r2 = _run_main(out2)
        assert r1.returncode == 0, r1.stderr
        assert r2.returncode == 0, r2.stderr
        assert out1.read_bytes() == out2.read_bytes(), "runs differ"
        assert out1.read_bytes() == IMAGE.read_bytes(), "copy != source"


if __name__ == "__main__":
    test_image_exists_and_matches_digest()
    test_image_dimensions()
    test_deterministic_two_runs()
    print("all entry tests passed")
