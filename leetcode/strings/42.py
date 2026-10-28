# Given a string containing just the characters '(' and ')', 
# return the length of the longest valid (well-formed) parentheses substring.

# use stack O(n)

s = ")()())"

# provides a boundary for calculating the length when a valid substring starts at index 0.
stack = [-1]
max_length = 0

for i in range(len(s)):

    if s[i] == '(':
        stack.append(i)

    else:
        stack.pop()

        if not stack:
            stack.append(i)
        else:
            length = i - stack[-1]
            max_length = max(max_length, length)

print(max_length)
