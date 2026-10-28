# Longest decreasing Subsequence


def lengthOfLDS(nums):
    n = len(nums)

    # Every element alone has subsequence length 1
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            # Current element must be smaller
            if nums[j] > nums[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(lengthOfLDS([9, 4, 3, 2, 5, 4, 3, 2]))  # 5
print(lengthOfLDS([5, 4, 3, 2, 1]))           # 5
print(lengthOfLDS([1, 2, 3, 4]))              # 1
