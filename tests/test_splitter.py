import pytest

from expense_splitter import split_evenly, split_weighted


# ---- split_evenly (already implemented) -------------------------------------

def test_even_divides_cleanly():
    assert split_evenly(9000, 3) == [3000, 3000, 3000]


def test_even_distributes_remainder_to_earliest():
    assert split_evenly(10000, 3) == [3334, 3333, 3333]
    assert sum(split_evenly(10000, 3)) == 10000


# ---- split_weighted (to be implemented) -------------------------------------

def test_weighted_simple_ratio():
    # 1:1:2 of 10000 -> 2500, 2500, 5000
    assert split_weighted(10000, [1, 1, 2]) == [2500, 2500, 5000]


def test_weighted_always_reconciles():
    # 1:1:1 of 10000 does not divide evenly into 3
    parts = split_weighted(10000, [1, 1, 1])
    assert sum(parts) == 10000
    assert all(isinstance(p, int) for p in parts)


def test_weighted_remainder_goes_to_largest_fraction():
    # 100 across weights 1:1:1 -> 34,33,33 (largest remainder gets the extra cent)
    parts = split_weighted(100, [1, 1, 1])
    assert sum(parts) == 100
    assert sorted(parts, reverse=True) == [34, 33, 33]


def test_weighted_rejects_empty_weights():
    with pytest.raises(ValueError):
        split_weighted(1000, [])


def test_weighted_rejects_nonpositive_total():
    with pytest.raises(ValueError):
        split_weighted(-1, [1, 2])
