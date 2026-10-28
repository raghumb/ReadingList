 # find longest common prefix

# approach 1 - Start with the first word as the candidate prefix. Shorten it until every word starts with it. \(O(nm)\)
def longest_common_prefix(words):
    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if prefix == "":
                return ""

    return prefix


words = ["flower", "flow", "flight"]
print(longest_common_prefix(words))  # fl

