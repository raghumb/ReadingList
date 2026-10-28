# Parse a string character-by-character to form a valid 32-bit signed integer. (atoi)

"""
    Convert a string into a 32-bit signed integer by following these rules:
1. Ignore leading spaces.
2. Read an optional + or - sign.
3. Read digits until a non-digit character appears.
4. If no digits are found, return 0.
5. Clamp the result to the 32-bit signed integer range.
    """
    
    
s = "   -42abc"

i = 0
n = len(s)

# 1. Skip leading spaces
while i < n and s[i] == ' ':
    i += 1

# 2. Read the sign
sign = 1

if i < n and s[i] == '-':
    sign = -1
    i += 1
elif i < n and s[i] == '+':
    i += 1

# 3. Read digits
number = 0

while i < n and s[i].isdigit():
    digit = int(s[i])
    number = number * 10 + digit
    i += 1

# 4. Apply the sign
number = number * sign

# 5. Clamp to 32-bit signed integer range
INT_MIN = -2**31
INT_MAX = 2**31 - 1

if number < INT_MIN:
    number = INT_MIN
elif number > INT_MAX:
    number = INT_MAX

print(number)