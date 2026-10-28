# Given two non-negative integers num1 and num2 represented as strings, 
# return the product of num1 and num2, also represented as a string.

num1 = "123"
num2 = "45"

m = len(num1)
n = len(num2)

# Maximum result length is m + n
result = [0] * (m + n)

# Multiply digits from right to left
for i in range(m - 1, -1, -1):
    for j in range(n - 1, -1, -1):

        digit1 = ord(num1[i]) - ord('0')
        digit2 = ord(num2[j]) - ord('0')

        product = digit1 * digit2

        # Positions in result array
        p1 = i + j
        p2 = i + j + 1

        total = product + result[p2]

        result[p2] = total % 10
        result[p1] += total // 10

# Remove leading zeros
i = 0
while i < len(result) - 1 and result[i] == 0:
    i += 1

# Convert digits to string
answer = ""

for digit in result[i:]:
    answer += str(digit)

print(answer)

