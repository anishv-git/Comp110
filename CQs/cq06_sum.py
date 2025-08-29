"""Summing the elements of a list using different loops"""

__author__ = "730773852"


def w_sum(vals: list[float]) -> float:

    idx = 0

    total = 0

    while idx < len(vals):
        total += vals[idx]
        idx += 1

    return total


def f_sum(vals: list[float]) -> float:

    sum: float = 0

    for val in vals:

        sum += val

    return sum


def f_range_sum(vals: list[float]) -> float:

    sum: float = 0.0
    for val in vals:
        sum += val
    return sum


print(f_range_sum([1.0, -0.9, 1.0]))
