# Variations of LPS

# Find the Index of the First Occurrence in a String

def compute_lps(pattern):
    m = len(pattern)
    lps = [0] * m

    length = 0
    i = 1

    while i < m:

        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1

        elif length > 0:
            length = lps[length - 1]

        else:
            lps[i] = 0
            i += 1

    return lps


def str_str(haystack, needle):

    if not needle:
        return 0

    n = len(haystack)
    m = len(needle)

    lps = compute_lps(needle)

    i = 0  # Pointer for haystack
    j = 0  # Pointer for needle

    while i < n:

        if haystack[i] == needle[j]:
            i += 1
            j += 1

            # Entire pattern matched
            if j == m:
                return i - j

        elif j > 0:
            j = lps[j - 1]

        else:
            i += 1

    return -1


# Input
haystack = "ababcabcabababd"
needle = "ababd"

print(str_str(haystack, needle))
