# 4Sum

"""
    Given an array nums of n integers, return an array of all the unique quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:

0 <= a, b, c, d < n
a, b, c, and d are distinct.
nums[a] + nums[b] + nums[c] + nums[d] == target
    """
    
# Sorting + Two Nested Loops + Two Pointers.
# O(n3)

nums = [1, 0, -1, 0, -2, 2]
target = 0

nums.sort()

n = len(nums)
result = []

for i in range(n - 3):

    # Skip duplicate first numbers
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    for j in range(i + 1, n - 2):

        # Skip duplicate second numbers
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue

        left = j + 1
        right = n - 1

        while left < right:

            total = nums[i] + nums[j] + nums[left] + nums[right]

            if total == target:

                result.append([
                    nums[i],
                    nums[j],
                    nums[left],
                    nums[right]
                ])

                left += 1
                right -= 1

                # Skip duplicate third numbers
                while left < right and nums[left] == nums[left - 1]:
                    left += 1

                # Skip duplicate fourth numbers
                while left < right and nums[right] == nums[right + 1]:
                    right -= 1

            elif total < target:
                left += 1

            else:
                right -= 1

print(result)


