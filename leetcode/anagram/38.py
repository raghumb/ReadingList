# Find All Anagrams in a String for a given substring

# find all starting indices in a string s where a substring is an anagram of string p.

s = "cbaebabacd"
p = "abc"

result = []

left = 0
k = len(p)

p_count = [0] * 26
window_count = [0] * 26

# Count characters in p
for ch in p:
    p_count[ord(ch) - ord('a')] += 1

for right in range(len(s)):
    # Add the incoming character
    window_count[ord(s[right]) - ord('a')] += 1

    # Remove the leftmost character if window is too large
    if right - left + 1 > k:
        window_count[ord(s[left]) - ord('a')] -= 1
        left += 1

    # Compare character frequencies
    if window_count == p_count:
        result.append(left)

print(result)