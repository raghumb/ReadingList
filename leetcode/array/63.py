# Find kth smallest element in array

# Use max heap

import heapq

def kth_smallest(arr, k):
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid array or k")

    heap = []

    for num in arr:
        heapq.heappush(heap, -num)

        if len(heap) > k:
            heapq.heappop(heap)

    return -heap[0]


numbers = [3, 2, 1, 5, 6, 4]

print(kth_smallest(numbers, 2))  # Output: 2