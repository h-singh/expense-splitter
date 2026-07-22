"""CLI entry point: python -m expense_splitter ..."""
from __future__ import annotations

import sys

from .splitter import split_evenly, split_weighted


def main(argv: list[str] | None = None) -> int:
    argv = argv if argv is not None else sys.argv[1:]
    if not argv:
        print("usage: expense_splitter {even|weighted} ...", file=sys.stderr)
        return 2

    mode, rest = argv[0], argv[1:]
    if mode == "even":
        total, num = int(rest[0]), int(rest[1])
        print(split_evenly(total, num))
    elif mode == "weighted":
        total = int(rest[0])
        weights = [int(w) for w in rest[1:]]
        print(split_weighted(total, weights))
    else:
        print(f"unknown mode: {mode}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
