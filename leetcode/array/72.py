# Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

nums = [100, 4, 200, 1, 3, 2]

num_set = set(nums)

max_length = 0

for num in num_set:

    # Start counting only if num is the
    # beginning of a consecutive sequence
    # Skip precedeccessor hence num-1
    if num - 1 not in num_set:

        current = num
        length = 1

        # Find consecutive numbers
        while current + 1 in num_set:
            current += 1
            length += 1

        max_length = max(max_length, length)

print(max_length)