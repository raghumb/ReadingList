1. Common anagram problem variations
1

Check whether two strings are anagrams
Example: "listen", "silent" → True
This is the basic problem. Use sorting or a character-frequency dictionary.



2

Ignore spaces, punctuation, and case
Example: "Dormitory!", "Dirty room" → True
Normalize the strings before comparing their character counts.



3

Check whether two strings are anagrams without sorting
Example: "aabbc", "abcab" → True
Use frequency counting. This tests whether you understand the \(O(n)\) approach.



4

Group anagrams from a list of words
Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
Output: [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]
Use a dictionary keyed by sorted characters or a character-frequency signature.



5

Find all anagrams of a pattern inside a string
Text: "cbaebabacd", pattern: "abc"
Output: starting indices [0, 6]
Use a sliding window and character frequencies rather than sorting every substring.



6

Check whether two strings can become anagrams with replacements
Example: "aab", "abb"
Answer: 1 replacement needed.
Count the excess characters in one string and determine the minimum changes required.



7

Find the minimum deletions needed to make two strings anagrams
Example: "abc" and "cde"
Answer: 4 deletions total.
Retain common character frequencies and delete the excess characters.



8

Check anagrams with Unicode or accented characters
Example: strings containing "é", "e", or combined accent characters.
Decide whether Unicode normalization should treat visually equivalent text as equivalent.


2. The key patterns behind these problems
Pattern	Used for
Sorting	Basic anagram check
Hash map / frequency counter	Linear-time anagram check
Dictionary with a signature key	Grouping anagrams
Sliding window	Finding anagrams inside a larger string
Frequency differences	Minimum replacements or deletions
Normalization	Case-insensitive, punctuation-insensitive, or Unicode-aware matching