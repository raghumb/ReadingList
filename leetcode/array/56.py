# 3Sum Closest

"""
    given an integer array nums of length n and an integer target.

Find three integers at distinct indices in nums such that the sum is closest to target.

Return the sum of the three integers.
    """
    
# Sorting + Two Pointers
# O(n2)


nums = [-1, 2, 1, -4]
target = 1

# Sorting allows us to decide which pointer to move 
# based on whether the sum is too small or too large
nums.sort()

n = len(nums)
closest_sum = nums[0] + nums[1] + nums[2]

# We fix one number using i and find the other two numbers using left and right.
for i in range(n - 2):

    left = i + 1
    right = n - 1

    while left < right:

        current_sum = nums[i] + nums[left] + nums[right]

        # Exact match: cannot get closer
        if current_sum == target:
            closest_sum = current_sum
            break

        # Update the closest sum
        if abs(current_sum - target) < abs(closest_sum - target):
            closest_sum = current_sum

        # Move pointers
        # Sum too small: increase left to get a larger sum.
        if current_sum < target:
            left += 1
        else:
            # Sum too large: decrease right to get a smaller sum.
            right -= 1

    if closest_sum == target:
        break

print(closest_sum)
