"""Mutating functions."""

__author__ = "730773852"


def manual_append(lst: list[int], num: int) -> None:
    """Appends an integer to the end of a list"""
    lst.append(num)


def double(lst: list[int]) -> None:
    """Doubles each element in the list."""
    i = 0
    while i < len(lst):
        lst[i] *= 2  # Multiply each element by 2
        i += 1


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print("list_1:", list_1)  # This will print the modified list
print("list_2:", list_2)  # This will also print the modified list
