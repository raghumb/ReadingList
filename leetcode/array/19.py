# Longest Increasing Subsequence

"""Given an integer array nums, return the length of the longest strictly increasing subsequence.

A subsequence is a sequence derived from an array by deleting some or no elements without changing the order of the remaining elements. 
For example, [3, 6, 2, 7] is a subsequence of [0, 3, 1, 6, 2, 2, 7].
Input: nums = [10, 9, 2, 5, 3, 7, 101, 18]

Output: 4

Explanation: The longest increasing subsequence is [2, 3, 7, 101], and its length is 4.

    """

def lengthOfLIS(arr):
    n = len(arr)

    # Every element forms an increasing subsequence of length 1
    dp = [1] * n

    for i in range(n):
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return max(dp)


print(lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]))  # 4
print(lengthOfLIS([0, 1, 0, 3, 2, 3]))            # 4
print(lengthOfLIS([7, 7, 7, 7]))                  # 1


