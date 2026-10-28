# Given a string s, partition s such that every substring of the partition is a palindrome.

# Return the minimum cuts needed for a palindrome partitioning of s

"""
    Example 1:

Input: s = "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
Example 2:

Input: s = "a"
Output: 0
Example 3:

Input: s = "ab"
Output: 1
 
    """
    

s = "aab"
n = len(s)

# Step 1: Store whether each substring is a palindrome
palindrome = [[False] * n for _ in range(n)]

# substring from i to j
# We process the table this way because, when checking a 
# longer substring, we may need to know whether its inner substring is already a palindrome.
for i in range(n - 1, -1, -1):
    for j in range(i, n):
        if s[i] == s[j]:
            # The substring has one or two characters.
            if j - i <= 1:
                palindrome[i][j] = True
            else:
                # The substring has more than two characters.
                palindrome[i][j] = palindrome[i + 1][j - 1]

# Step 2: Find minimum cuts
cuts = [0] * n

for i in range(n):
    cuts[i] = i  # Worst case: every character is separate

    for j in range(i + 1):
        if palindrome[j][i]:
            # The palindrome starts at index 0
            # If the entire prefix s[0:i+1] is a palindrome, we need zero cuts.
            if j == 0:
                cuts[i] = 0
            else:
                cuts[i] = min(cuts[i], cuts[j - 1] + 1)

print(cuts[n - 1])
