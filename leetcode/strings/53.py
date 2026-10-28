# Edit distance

"""
    Edit Distance asks for the minimum number of operations needed to convert one string into another.

You can perform three operations:
1. Insert a character.
2. Delete a character.
3. Replace a character.
    """
    

word1 = "horse"
word2 = "ros"

m = len(word1)
n = len(word2)

dp = [[0] * (n + 1) for _ in range(m + 1)]

# Convert word1 prefix to an empty string: delete all characters
for i in range(m + 1):
    dp[i][0] = i

# Convert an empty string to word2 prefix: insert all characters
for j in range(n + 1):
    dp[0][j] = j

for i in range(1, m + 1):
    for j in range(1, n + 1):

        if word1[i - 1] == word2[j - 1]:
            dp[i][j] = dp[i - 1][j - 1]

        else:
            insert_op = dp[i][j - 1]
            delete_op = dp[i - 1][j]
            replace_op = dp[i - 1][j - 1]

            dp[i][j] = 1 + min(
                insert_op,
                delete_op,
                replace_op
            )

print("Edit distance:", dp[m][n])
