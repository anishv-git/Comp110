__author__ = "730773852"


from find_max import find_and_remove_max


def test_find_and_remove_max_case_1() -> None:
    nums: list[int] = [1, 2, 3, 4, 5]
    result = find_and_remove_max(nums)
    assert result == 5
    assert nums == [1, 2, 3, 4]


def test_find_and_remove_max_case_2() -> None:
    nums: list[int] = [-1, -2, -3, -4, -5]
    result = find_and_remove_max(nums)
    assert result == -1
    assert nums == [-2, -3, -4, -5]


def test_find_and_remove_max_case_3() -> None:
    nums: list[int] = [10, 10, 10]
    result = find_and_remove_max(nums)
    assert result == 10
    assert nums == []
