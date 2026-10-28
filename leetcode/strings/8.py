# find longest common substring

# DP, \(O(mn)\)
# in dp table, The nonzero diagonal values show matching characters that extend a consecutive substring. 

def longest_common_substring(s1, s2):
    m, n = len(s1), len(s2)

    # dp[i][j] = length of the common substring
    # ending at s1[i-1] and s2[j-1]
    
    # 2D table (a list of lists) filled with zeros.
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    max_length = 0
    end_index = 0

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1

                if dp[i][j] > max_length:
                    max_length = dp[i][j]
                    end_index = i
            else:
                dp[i][j] = 0

    substring = s1[end_index - max_length:end_index]
    return substring, max_length


s1 = "abcdeccd"
s2 = "abccfcde"

result, length = longest_common_substring(s1, s2)

print("Substring:", result)  # abc
print("Length:", length)    # 3
