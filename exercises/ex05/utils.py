"""Function utility activity - EX05"""

__author__ = "730773852"


def only_evens(nums: list[int]) -> list[int]:
    """Returns only the even numbers in the list"""
    result: list[int] = []
    for num in nums:
        if num % 2 == 0:
            result.append(num)
    return result


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Outputs a list from a certain range"""
    result: list[int] = []

    if start < 0:
        start = 0

    if end > len(input):
        end = len(input)

    if len(input) == 0 or start >= len(input) or end <= 0:
        return result

    for idx in range(start, end):
        result.append(input[idx])

    return result


def add_at_index(input: list[int], elem: int, idx_num: int) -> None:
    """Insert element at the specified index in the list."""
    if idx_num < 0 or idx_num > len(input):
        raise IndexError("Index is out of bounds for the input list")

    input.append(0)

    for i in range(len(input) - 1, idx_num, -1):
        input[i] = input[i - 1]

    input[idx_num] = elem
