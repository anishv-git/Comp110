"""exercise 04 utility functions"""

__author__ = "730773852"


def all(int_list: list[int], int: int) -> bool:
    """Helps check if all int's in a list are the same"""
    if len(int_list) == 0:
        return False

    for ints in int_list:
        if ints != int:
            return False

    return True


def max(num_list: list[int]) -> int:
    """Shows the largest number out of a list"""
    if len(num_list) == 0:
        print("max() arg is an empty List")

    largest = num_list[0]
    for num in num_list:
        if num > largest:
            largest = num
    return largest


def is_equal(list1: list[int], list2: list[int]) -> bool:
    """To make sure a list is equal to one another"""
    if list1 == list2:
        return True
    else:
        return False


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Adds value to a certain list"""
    for x in list_2:
        list_1.append(x)
