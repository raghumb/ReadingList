# maximum number of ones - I

# Find the longest sequence of consecutive 1s in a binary array.


nums = [1, 1, 0, 1, 1, 1]

count = 0
max_count = 0

for num in nums:

    if num == 1:
        count = count + 1
    else:
        count = 0

    max_count = max(max_count, count)

print(max_count)


