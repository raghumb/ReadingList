# Given a string, S. Find the length of the longest substring without repeating characters.
# use sliding window O(n)

def longest_substring(s):
    seen = set()
    left = 0
    max_length = 0

 
    """

    Suppose the current window is "abcd" and the next character is b.
The window would become "abcdb", which has a duplicate b.
We must remove characters from the left:
1. Remove a → window "bcd". The old b is still in seen.
2. Remove b → window "cd". Now the duplicate is gone.
3. Add the new b → window "cdb".
A while loop keeps removing characters until the window becomes valid again.
    """
    
    for right in range(len(s)):
        while s[right] in seen:
            seen.remove(s[left])
            left += 1

        seen.add(s[right])

        max_length = max(max_length, right - left + 1)

    return max_length

s = "abcabcbb"
print(longest_substring(s))
