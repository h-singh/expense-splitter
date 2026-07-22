# expense-splitter

A tiny CLI + library for splitting shared expenses among people.

## Current features
- `split_evenly(total_cents, num_people)` — split a bill into equal parts.

## What needs implementing
`split_weighted(total_cents, weights)` is **stubbed out** and its tests are
failing. Implement it so that:

1. Each person's share is proportional to their weight.
2. All amounts are whole **cents** (integers) — no fractional cents.
3. The parts **always reconcile**: `sum(parts) == total_cents` exactly, even when
   the proportional split doesn't divide evenly.
4. Leftover cents (from rounding) are distributed deterministically and fairly.

Run the tests:

```bash
python -m pytest -q
```

## CLI

```bash
python -m expense_splitter even 10000 3
python -m expense_splitter weighted 10000 1 1 2
```
