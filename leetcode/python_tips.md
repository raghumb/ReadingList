- write down edge cases
- finding sum of first k elements: sum(arr[:k])
- finding max: max(a,b)
- array sort: arr.sort(reverse=True). in place sorting.
- dictionary get: dict.get(key, 0) -> 0 is default value. key can be character
- dictionary set: dict[key] = val
- init 2d array with zeros. dp = [[0] * (n + 1) for _ in range(m + 1)]
```
simple version:
dp = []

for i in range(m + 1):
    row = [0] * (n + 1)
    dp.append(row)
```
- Remove last char from a word. w[:-1]
- The key idea is that anagrams produce the same string when their characters are sorted.
- sorted(word) , creates a array of each character sorted. eg, "tea", -> ["a", "e", "t"]
- combine elements of an array into a string. "".join(arr)
- convert string to lower case. word.lower()
- List comprehension example:
```
 nums = [board[row][col] for row in range(9)
                if board[row][col] != '.']

```

Simplified:
```
for col in range(9):
    nums = []

    for row in range(9):
        if board[row][col] != '.':
            nums.append(board[row][col])

    if len(nums) != len(set(nums)):
        return False
```
- List comprehension example: create a array of squared numbers
```
squares = []

for n in range(5):
    squares.append(n * n)
```

General syntax
```
[expression for item in iterable if condition]
```
```
squares = [n * n for n in range(5)]
```

- get character from string. s[i]
- array substring: a[:k] -> first k elements. a[k:] -> last k elements. a[k:m] ->  k to m-1 elements
- looping thru array when index is not required: for num in arr:
- assign +/-ve infinity to a variable: float('-inf')
- convert char to integer. ord(ch)
- check if char is int. ch.isdigit()
- convert integer to char. chr(ch)



# Merging
- Two intervals overlap if they share at least one common point (i.e. start₂ ≤ end₁ and start₁ ≤ end₂). but if we sort by end, we need not compare second condition.

## Sorted by start
```
if current_start <= previous_end:
    # Overlap
```

## Sorted by end
```
if current_start < last_end:
    # Overlap
```

sorting by start helps you merge intervals; sorting by end helps you choose which intervals to keep.

- arr[-1] → Returns the last element of the list.
- arr[:-1] → Returns a new list containing all elements except the last one


** IMP ***

For converting string A into string B:
- Deletions = len(A) - LCS (Source - LCS)
- Insertions = len(B) - LCS (Target - LCS)

