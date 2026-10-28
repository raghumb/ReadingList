# find longest common subsequence

def longest_common_subsequence(s1, s2):
    m = len(s1)
    n = len(s2)

    # Create a table filled with zeros
    dp = []

    for i in range(m + 1):
        row = [0] * (n + 1)
        dp.append(row)

    # Fill the table
    for i in range(1, m + 1):
        for j in range(1, n + 1):

            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

            else:
                dp[i][j] = max(
                    dp[i - 1][j],
                    dp[i][j - 1]
                )

    return dp[m][n]


s1 = "abcde"
s2 = "ace"

print(longest_common_subsequence(s1, s2))  # 3

