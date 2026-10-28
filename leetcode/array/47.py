# Check if you can split an array into two non-empty parts with equal sums.

# O(n)

nums = [1, 2, 3, 6]

total = sum(nums)
left_sum = 0
found = False

for i in range(len(nums) - 1):
    left_sum += nums[i]
    right_sum = total - left_sum

    if left_sum == right_sum:
        found = True
        break

print(found)