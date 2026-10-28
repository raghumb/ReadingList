# Two Sum
# Given an array of integers nums and an integer target. Return the indices(0 - indexed)
# of two elements in nums such that they add up to target.

def two_sum(nums, target):
    seen = {}

    for i in range(len(nums)):
        required = target - nums[i]

        if required in seen:
            return [seen[required], i]

        seen[nums[i]] = i

    return []

nums = [2, 7, 11, 15]
target = 17

print(two_sum(nums, target))