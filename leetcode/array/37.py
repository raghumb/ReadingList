# Top K Frequent Elements
def topKFrequent(nums, k):
    freq = {}

    # Count frequency of each number
    for num in nums:
        freq[num] = freq.get(num, 0) + 1

    # Sort numbers by frequency, highest first
    sorted_nums = sorted(freq, key=lambda x: freq[x], reverse=True)

    return sorted_nums[:k]


# Hardcoded input
nums = [1, 1, 1, 2, 2, 3]
k = 2

print(topKFrequent(nums, k))