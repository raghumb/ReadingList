# Minimum deletions to make two strings anagrams

s = "abc"
t = "amn"

count = [0] * 26

# Count characters in s
for ch in s:
    count[ord(ch) - ord('a')] += 1

# Subtract characters in t
for ch in t:
    count[ord(ch) - ord('a')] -= 1

# Calculate total deletions
deletions = 0

for value in count:
    # A positive value means the character occurs more often in s.
    # A negative value means it occurs more often in t.
    # Zero means the character counts match.
    # We must delete the excess characters from whichever string has more of them. 
    # The absolute value counts those excess characters regardless of which string they belong to.
    deletions += abs(value)

print(deletions)