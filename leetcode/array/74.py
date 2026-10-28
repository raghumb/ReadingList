# Maximum Gap
"""
    Given an integer array nums, return the maximum difference between two successive elements in its sorted form. If the array contains less than two elements, return 0.

You must write an algorithm that runs in linear time and uses linear extra space.
    """

# O(nlogn) solution
nums = [3, 6, 9, 1]

if len(nums) < 2:
    print(0)
else:
    nums.sort()

    max_gap = 0

    for i in range(1, len(nums)):
        gap = nums[i] - nums[i - 1]
        max_gap = max(max_gap, gap)

    print(max_gap)