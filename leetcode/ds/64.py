# Min heap from scratch

class MinHeap:
    def __init__(self):
        self.heap = []

    def push(self, val):
        # append new element
        self.heap.append(val)

        # Move element upward (heapify up)
        # Find the new element's index
        i = len(self.heap) - 1

        # Keep moving up until reaching the root
        while i > 0:
            # Find the parent
            parent = (i - 1) // 2

            # condition satisfied
            if self.heap[parent] <= self.heap[i]:
                break
            
            # swap parent and current
            self.heap[parent], self.heap[i] = self.heap[i], self.heap[parent]
            
            # Continue from the parent's position
            i = parent

    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        # Remove the root and next step Replace root with last
        smallest = self.heap[0]

        # Move last element to root
        self.heap[0] = self.heap.pop()

        # Move root downward (heapify down)
        i = 0
        n = len(self.heap)

        while True:
            # Find both children
            left = 2 * i + 1
            right = 2 * i + 2
            smallest_index = i

            # Does the left child exist? and min heap property check
            if left < n and self.heap[left] < self.heap[smallest_index]:
                smallest_index = left

            if right < n and self.heap[right] < self.heap[smallest_index]:
                smallest_index = right

            if smallest_index == i:
                break

            self.heap[i], self.heap[smallest_index] = (
                self.heap[smallest_index],
                self.heap[i]
            )

            i = smallest_index

        return smallest

    def peek(self):
        if not self.heap:
            return None

        return self.heap[0]


# Example
heap = MinHeap()

for num in [5, 3, 8, 1, 4]:
    heap.push(num)

print(heap.heap)  # [1, 3, 8, 5, 4]

print(heap.peek())  # 1
print(heap.pop())   # 1
print(heap.pop())   # 3
print(heap.heap)    # [4, 5, 8]