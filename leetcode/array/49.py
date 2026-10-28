# maximum averge subarray

# Sliding window

nums = [1, 12, -5, -6, 50, 3]
k = 4

# Calculate the sum of the first window
window_sum = sum(nums[:k])
max_sum = window_sum

# Slide the window
for i in range(k, len(nums)):
    window_sum = window_sum + nums[i] - nums[i - k]

    max_sum = max(max_sum, window_sum)

print(max_sum / k)
