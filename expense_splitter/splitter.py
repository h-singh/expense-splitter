"""Core expense-splitting logic.

All monetary amounts are expressed in integer **cents** to avoid floating-point
money bugs.
"""
from __future__ import annotations

from typing import List


def split_evenly(total_cents: int, num_people: int) -> List[int]:
    """Split ``total_cents`` into ``num_people`` parts as evenly as possible.

    The parts always sum back to ``total_cents``. Any leftover cents are handed,
    one each, to the earliest people.
    """
    if num_people <= 0:
        raise ValueError("num_people must be positive")
    if total_cents < 0:
        raise ValueError("total_cents must be non-negative")

    base, remainder = divmod(total_cents, num_people)
    return [base + (1 if i < remainder else 0) for i in range(num_people)]


def split_weighted(total_cents: int, weights: List[int]) -> List[int]:
    """Split ``total_cents`` proportionally to ``weights`` (see README).

    NOT IMPLEMENTED YET — this is the pre-task feature. It must return a list of
    integer cents, proportional to ``weights``, that sums exactly to
    ``total_cents``.
    """
    raise NotImplementedError("split_weighted is not implemented yet")
