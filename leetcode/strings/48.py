# Find the Closest Palindrome

"""
    Given a string n representing an integer, 
    return the closest integer (not including itself), which is a palindrome. If there is a tie, return the smaller one.
    """
    
"""
    Input n	Output	Explanation
"123"	"121"	Distance 2; closer than 131
"1"	"0"	0 is closer than 2
"10"	"9"	9 is closer than 11
"99"	"101"	Distance 2; 88 is farther away

The important edge cases are numbers like 1, 10, 99, 100, and 1000, where the closest palindrome 
may have a different number of digits.
    """
    
# O(L)

"""Solution:
    candidate generation
Instead of checking every number, we generate only a few palindrome candidates around the input.
    """

n = "123"

length = len(n)
num = int(n)

# Take the first half, including the middle digit if odd
# Because the first half determines the entire palindrome.
prefix = int(n[:(length + 1) // 2])

candidates = set()

# Boundary candidates for digit-length changes
"""
    Why are these important?
- For "1000", the closest palindrome can be "999" — one fewer digit.
- For "99", the closest palindrome can be "101" — one more digit.
    """
candidates.add(10 ** (length - 1) - 1)
candidates.add(10 ** length + 1)

# Try the prefix and its two neighbors
# The closest palindrome usually comes from mirroring the original prefix or a prefix just one smaller or one larger.
for p in (prefix - 1, prefix, prefix + 1):
    if p < 0:
        continue

    left = str(p)

    if length % 2 == 0:
        # If the original number has an even number of digits, reverse the entire prefix and append it.
        palindrome = left + left[::-1]
    else:
        # If the original number has an odd number of digits, do not duplicate the middle digit.
        # remove last char and reverse
        
        palindrome = left + left[:-1][::-1]

    candidates.add(int(palindrome))

# Exclude the original number
candidates.discard(num)

# Closest palindrome; smaller number wins a tie
# abs(x - num) — the absolute distance from the input.
# x — the smaller number wins if two candidates have the same distance.
answer = min(candidates, key=lambda x: (abs(x - num), x))

print(str(answer))
