# Subset sum equals to target

# Given an array arr of n integers and an integer target, determine 
# if there is a subset of the given array with a sum equal to the given target.

def subset_sum(arr, target):
    dp = [False] * (target + 1)
    dp[0] = True

    for num in arr:
        for current_sum in range(target, num - 1, -1):
            dp[current_sum] = (
                dp[current_sum] or dp[current_sum - num]
            )

    return dp[target]


arr = [2, 3, 7, 8, 10]
target = 11

print(subset_sum(arr, target))  # True