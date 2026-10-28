# Find First and Last Position of Element in Sorted Array

"""
    Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.
    """

# Binary Search twice

# We need to find:
# 1. The first occurrence of target.
# 2. The last occurrence of target.


nums = [5, 7, 7, 8, 8, 10]
target = 8

n = len(nums)

first = -1
last = -1

# Binary search to find first occurrence
left = 0
right = n - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        first = mid
        right = mid - 1  # Continue searching left

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


# Binary search to find last occurrence
left = 0
right = n - 1

while left <= right:

    mid = (left + right) // 2

    if nums[mid] == target:
        last = mid
        left = mid + 1  # Continue searching right

    elif nums[mid] < target:
        left = mid + 1

    else:
        right = mid - 1


print([first, last])

