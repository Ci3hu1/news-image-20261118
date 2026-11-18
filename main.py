#!/usr/bin/env python3
"""Write the verified front page to /output/entry.png.

Reads news.png next to this script, checks that it is the expected
1024x1024 PNG (signature, dimensions, size and SHA-256 digest), then
copies the verified bytes to /output/entry.png. Pure standard library,
no network; running it twice writes identical bytes.
"""

import argparse
import hashlib
import os
import struct
import sys

SOURCE_NAME = "news.png"
DEFAULT_TARGET = "/output/entry.png"

EXPECTED_WIDTH = 1024
EXPECTED_HEIGHT = 1024
MAX_BYTES = 1024 * 1024
EXPECTED_DIGEST = "c26a547e0eff571bcf86ad48616e96dcffae7b70247cc19ce4a66925aa6f8edc"

PNG_MAGIC = b"\x89PNG\r\n\x1a\n"


def fail(message):
    print("error: " + message, file=sys.stderr)
    sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Write the verified front page to an output PNG."
    )
    parser.add_argument(
        "--output",
        default=DEFAULT_TARGET,
        help="where to write the verified image (default: %(default)s)",
    )
    args = parser.parse_args()
    target_path = args.output

    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, SOURCE_NAME)

    try:
        with open(source, "rb") as handle:
            data = handle.read()
    except OSError as exc:
        fail("cannot read %s: %s" % (source, exc))

    if len(data) > MAX_BYTES:
        fail(
            "%s is %d bytes, over the %d-byte limit"
            % (SOURCE_NAME, len(data), MAX_BYTES)
        )

    if data[:8] != PNG_MAGIC:
        fail("%s does not start with the PNG signature" % SOURCE_NAME)

    if len(data) < 24:
        fail("%s is too short to hold a PNG header" % SOURCE_NAME)

    width, height = struct.unpack(">II", data[16:24])
    if (width, height) != (EXPECTED_WIDTH, EXPECTED_HEIGHT):
        fail(
            "%s is %dx%d, expected %dx%d"
            % (SOURCE_NAME, width, height, EXPECTED_WIDTH, EXPECTED_HEIGHT)
        )

    digest = hashlib.sha256(data).hexdigest()
    if digest != EXPECTED_DIGEST:
        fail(
            "%s digest %s does not match the expected %s"
            % (SOURCE_NAME, digest, EXPECTED_DIGEST)
        )

    target_dir = os.path.dirname(target_path)
    try:
        os.makedirs(target_dir, exist_ok=True)
        with open(target_path, "wb") as handle:
            handle.write(data)
    except OSError as exc:
        fail("cannot write %s: %s" % (target_path, exc))

    print(
        "wrote %s (%d bytes, sha256 %s)"
        % (target_path, len(data), digest)
    )


if __name__ == "__main__":
    main()
