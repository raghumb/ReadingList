# Group Anagrams: Given an array of strings, group the anagrams together.
# O(nklogk)

def group_anagrams(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))
        # create empty list if sorted key is not found
        if key not in groups:
            groups[key] = []

        # append the word to the already created list
        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))


"""Use a character-frequency tuple as the key. For lowercase English letters, each word gets a tuple of 26 character counts.
O(nk)
    """
    
# Create a list of 26 zeros    
# Each position represents a lowercase English letter.
# Convert each character into an index
# Convert the list into a tuple. Dictionary keys must be hashable. A list is mutable and cannot be used as a dictionary key, but a tuple of integers can.
# 

def group_anagrams_2(words):
    groups = {}

    for word in words:
        counts = [0] * 26

        for char in word:
            index = ord(char) - ord('a')
            counts[index] += 1

        key = tuple(counts)

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())


words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams_2(words))
