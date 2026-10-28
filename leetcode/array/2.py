 # kth largest element in an array
 
 # approach 1- sort array in reverse order and find arr[k - 1]. O(nlogn)
 
 # approach 2- use min heap. O(nlog k)
 
"""

A min-heap is a data structure where the smallest element is always at the top of the tree/each sub tree.
pop will remove smallest element.
heapq.heappush(heap, num) rearranges the heap list when necessary to maintain the min-heap property.
heapq.heappop() removes and returns the smallest element in the heap.
          1
    |.       |
    3        8
  |   |
  5.  4
    

"""
 
import heapq

def kth_largest(arr, k):
    if not arr or k < 1 or k > len(arr):
        raise ValueError("Invalid array or k")

    heap = []

    for num in arr:
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    return heap[0]


numbers = [3, 2, 1, 5, 6, 4]

print(kth_largest(numbers, 2))  # Output: 5 
 