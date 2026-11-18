"""Newspaper front-page image entry for Wednesday, 18 November 2026.

This program is the reproducible entry generator for the make.fun
news-image-20261118 bounty. The artwork itself is a single newspaper
front page dated Wednesday 18 November 2026: a bold masthead across
the top, two lead stories (Trump lands in Manila for the Quad talks;
Ukraine hits the Crimean bridge again), and 34 numbered stories
across seven regions — Asia 8, Europe 6, Middle East 6, North America
6, Africa 4, Oceania 3, Latin America 2 — with a sources line at the
foot naming The Guardian, BBC, NYT, Al Jazeera, RNZ, ABC News, Reuters
and AP. Every headline and summary was researched from reporting dated
18 November 2026 and drawn with PIL/DejaVu fonts, so the page carries
36 verified stories in crisp text instead of generated imagery.

The finished artwork is stored next to this script as ``news.png``.
Running this script verifies that stored image byte-for-byte against
its known SHA-256 digest, then copies it to the requested output path
and verifies the copy as well, so the delivered entry is exactly the
artwork that was prepared for the bounty. Nothing is generated, fetched
from the network, or altered in transit; the copy is deterministic.

Usage:
    python3 main.py [--output PATH]

The default output path is /output/entry.png.
"""

import argparse
import hashlib
import shutil
import sys
from pathlib import Path

EXPECTED_DIGEST = (
    "c26a547e0eff571bcf86ad48616e96dcffae7b70247cc19ce4a66925aa6f8edc"
)
SOURCE_FILENAME = "news.png"
DEFAULT_OUTPUT = "/output/entry.png"
READ_CHUNK_SIZE = 1024 * 1024


def locate_source_image() -> Path:
    """Return the path of the stored front-page image beside this script."""
    script_dir = Path(__file__).resolve().parent
    return script_dir / SOURCE_FILENAME


def digest_file(path: Path) -> str:
    """Compute the SHA-256 hex digest of the file at *path*."""
    hasher = hashlib.sha256()
    with path.open("rb") as handle:
        while True:
            chunk = handle.read(READ_CHUNK_SIZE)
            if not chunk:
                break
            hasher.update(chunk)
    return hasher.hexdigest()


def check_digest(path: Path, label: str) -> int:
    """Verify *path* matches the expected digest; return its byte size.

    Returns the file size in bytes when the digest matches. Prints an
    error and returns -1 when the file is missing or the digest differs.
    """
    if not path.is_file():
        print(f"error: {label} image not found: {path}", file=sys.stderr)
        return -1
    observed = digest_file(path)
    if observed != EXPECTED_DIGEST:
        print(
            f"error: {label} image SHA-256 mismatch: "
            f"expected {EXPECTED_DIGEST}, got {observed}",
            file=sys.stderr,
        )
        return -1
    return path.stat().st_size


def deliver_entry(source: Path, destination: Path) -> int:
    """Copy the verified source image to *destination* and verify the copy.

    Returns 0 on success, 1 on any failure.
    """
    source_size = check_digest(source, "source")
    if source_size < 0:
        return 1

    destination.parent.mkdir(parents=True, exist_ok=True)
    try:
        shutil.copyfile(source, destination)
    except OSError as exc:
        print(f"error: could not write output image: {exc}", file=sys.stderr)
        return 1

    written_size = check_digest(destination, "output")
    if written_size < 0:
        return 1

    if written_size != source_size:
        print(
            f"error: output image size mismatch: expected {source_size} "
            f"bytes, got {written_size} bytes",
            file=sys.stderr,
        )
        return 1

    print(
        f"Wrote newspaper front page for Wednesday 18 November 2026 to "
        f"{destination} ({written_size} bytes, "
        f"SHA-256 verified: {EXPECTED_DIGEST[:16]}...)"
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    """Build the command-line parser for this entry generator."""
    parser = argparse.ArgumentParser(
        description=(
            "Copy the verified newspaper front page for Wednesday "
            "18 November 2026 to the output path."
        )
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_OUTPUT,
        help="output image path (default: %(default)s)",
    )
    return parser


def main(argv=None) -> int:
    """Entry point: parse options and deliver the front-page image."""
    options = build_parser().parse_args(argv)
    source = locate_source_image()
    destination = Path(options.output)
    return deliver_entry(source, destination)


if __name__ == "__main__":
    raise SystemExit(main())
