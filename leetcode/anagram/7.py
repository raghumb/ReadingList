# find if one string is anagram of another

"""
    An anagram is a word or string
    formed by rearranging the characters of another string, using every character the same number of times.
    "listen" and "silent" → Anagrams
    """
    
# approach 1 - sort two list and compare them s1==s2. O(nlogn)
# approach 2 - count how many times each character appears.  O(n)


    
def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq:
            return False

        freq[ch] -= 1

        if freq[ch] < 0:
            return False

    return True


print(are_anagrams("listen", "silent"))  # True
print(are_anagrams("aabb", "abbb"))      # False
    
    