# Longest Palindromic Subsequence

s = "bbbab"

# O(n2)

n = len(s)

dp = [[0] * n for _ in range(n)]

# Every single character is a palindrome of length 1
for i in range(n):
    dp[i][i] = 1

# Check substrings of increasing length
# Because a longer substring depends on answers for shorter substrings.
for outer in range(2, n + 1):
    for i in range(n - outer + 1):
        j = i + outer - 1
        # If the outer characters match, we can include both in the palindrome.
        # The 2 accounts for these two matching characters.
        if s[i] == s[j]:
            dp[i][j] = 2 + dp[i + 1][j - 1]
        else:
            dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

print(dp[0][n - 1])