# maximum number of ones - II

# Find the longest sequence of 1s if you can flip at most k zeros.

# Sliding window


nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
k = 2

left = 0
zeros = 0
max_length = 0

for right in range(len(nums)):

    if nums[right] == 0:
        zeros += 1

    while zeros > k:
        if nums[left] == 0:
            zeros -= 1

        left += 1

    length = right - left + 1
    max_length = max(max_length, length)

print(max_length)
