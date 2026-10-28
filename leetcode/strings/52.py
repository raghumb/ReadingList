# Minimum Insertions and Deletions to Convert String A to String B

"""
    A cleaner way to calculate the minimum is to identify the characters that can be kept in the same relative order.

The Longest Common Subsequence of "heap" and "pea" is "ea", with length 2.
- Deletions = len(A) - LCS = 4 - 2 = 2
- Insertions = len(B) - LCS = 3 - 2 = 1
Total operations = 2 + 1 = 3.
    """
    

A = "heap"
B = "pea"

m = len(A)
n = len(B)

dp = [[0] * (n + 1) for _ in range(m + 1)]

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if A[i - 1] == B[j - 1]:
            dp[i][j] = 1 + dp[i - 1][j - 1]
        else:
            dp[i][j] = max(
                dp[i - 1][j],
                dp[i][j - 1]
            )

lcs = dp[m][n]

deletions = m - lcs
insertions = n - lcs

print("LCS length:", lcs)
print("Deletions:", deletions)
print("Insertions:", insertions)
print("Total operations:", deletions + insertions)
