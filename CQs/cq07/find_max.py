"""find and remove max in list functions"""

__author__ = "730773852"


def find_and_remove_max(nums: list[int]) -> int:
    if len(nums) == 0:
        return -1

    # Find the maximum value manually
    max_value = nums[0]
    for num in nums:
        if num > max_value:
            max_value = num

    # Create a new list without the maximum value
    idx = 0
    while idx < len(nums):
        if nums[idx] == max_value:
            nums.pop(idx)
        else:
            idx += 1

    return max_value
