"""testing the functions"""

__author__ = "730773852"


import pytest

from utils import only_evens, sub, add_at_index


# only_evens tests
def test_only_evens_use_case_1_and_2() -> None:
    """Test only_evens with an empty list, a full list, and a list without any evens"""
    assert only_evens([1, 3, 5, 7]) == []
    assert only_evens([1, 2, 3, 4, 5, 6]) == [2, 4, 6]


def test_only_evens_edge_case_1() -> None:
    assert only_evens([]) == []


# sub tests
def test_sub_use_case_1and2() -> None:
    """Test sub with an empty list, a full list, and and negative start list"""
    assert sub([10, 20, 30, 40, 50], 1, 4) == [20, 30, 40]
    assert sub([10, 20, 30, 40], -3, 10) == [10, 20, 30, 40]


def test_sub_edge_case_1() -> None:
    assert sub([], 1, 3) == []


def test_add_at_index():
    """Checks if function fully works"""
    list_1 = [1, 2, 3, 5]
    add_at_index(list_1, 4, 3)
    assert list_1 == [1, 2, 3, 4, 5]
    with pytest.raises(IndexError):  # use of this helps with the index error
        add_at_index(list_1, 0, -1)
