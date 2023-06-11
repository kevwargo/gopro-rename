import re
from argparse import ArgumentParser
from pathlib import Path

GOPRO_REGEXP = re.compile(r"^(G[HXL])([0-9]{2})([0-9]{4})\.(LRV|MP4|THM)")


def run():
    args = parse_args()
    process_fn = print if args.dry_run else rename
    for f in args.path.iterdir():
        if not (m := GOPRO_REGEXP.match(f.name)):
            continue
        chapter, number = map(int, [m.group(2), m.group(3)])
        header, ext = m.group(1), m.group(4).lower()
        newname = args.path / f"{header}_{number:04d}_{chapter:02d}.{ext}"
        process_fn(f, newname)


def rename(src: Path, dst: Path):
    src.rename(dst)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument("-n", "--dry-run", action="store_true")
    parser.add_argument("path", type=Path)
    return parser.parse_args()
