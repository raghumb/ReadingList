# Shortest Palindrome - given a string s, convert s to a palindrome by adding characters in front of it.

# make the string a palindrome by adding the minimum number of characters to the beginning. You cannot add characters to the end.

# Approach 1, O(n2)

"""

For "abcd", the longest palindromic prefix is just "a". 
The remaining substring is "bcd", so reverse it to get "dcb".


"""


s = "abcd"

i = len(s)

"""The key idea is to find the longest palindromic prefix of the string. 
    Whatever remains after that prefix must be reversed and added to the beginning.
    """

while i > 0:
    prefix = s[:i]

    if prefix == prefix[::-1]:
        break

    i -= 1

remaining = s[i:]
result = remaining[::-1] + s

print(result)

# # Approach 2 - O(n)

"""
    
    The key idea is to use the KMP prefix function, also called the LPS (Longest Prefix Suffix) 
    array, 
    to find the longest palindromic prefix without checking every substring.
    it helps us discover how many characters at the beginning of the string form a palindrome.
    """
    

s = "abcd"

# Reverse the string
rev = s[::-1]

# Combine the string, separator, and reversed string
combined = s + "#" + rev

#Why use the original string followed by its reverse? A prefix of s that matches 
# a suffix of rev corresponds to a prefix of s that reads the same forwards and backwards.
# lps[i] stores
# the longest proper prefix that is also a suffix for the substring ending at index i.
# 

# Build the LPS array
lps = [0] * len(combined)

length = 0
i = 1

while i < len(combined):
    if combined[i] == combined[length]:
        # Extend the current matching prefix by one character, record its length, and move forward.
        length += 1
        lps[i] = length
        i += 1
    else:
        # Characters differ, but a previous match exists
        # Do not immediately reset length to zero. Instead, 
        # fall back to a shorter prefix that might still match. This is the key optimization in KMP.
        if length != 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

# The last LPS value is the longest palindromic prefix length
palindrome_length = lps[-1]

# Add the reversed non-palindromic suffix to the front
result = s[palindrome_length:][::-1] + s

print(result)
