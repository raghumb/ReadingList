# Longest Palindromic Substring

"""Expand Around Center. 
    It checks every position in the string as a possible palindrome center and 
    expands outward while the characters match.
    """
    
def longestPalindrome(s):
    result = ""

    for i in range(len(s)):
        # Odd-length palindrome: center is one character
        left = right = i

        while left >= 0 and right < len(s) and s[left] == s[right]:
            # check if its longest, right - left + 1 is length of current palindrome. len(result) is previous length
            if right - left + 1 > len(result):
                result = s[left:right + 1]

            left -= 1
            right += 1

        # Even-length palindrome: center is between two characters
        left = i
        right = i + 1

        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > len(result):
                result = s[left:right + 1]

            left -= 1
            right += 1

    return result


print(longestPalindrome("bbabadaa"))  # bab or aba
print(longestPalindrome("cbbd"))   # bb


