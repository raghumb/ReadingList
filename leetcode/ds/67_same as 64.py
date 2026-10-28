# priority queue from scratch

# A priority queue is commonly implemented using a binary heap.

class PriorityQueue:
    def __init__(self):
        self.heap = []

    # Insert element
    def push(self, val):
        self.heap.append(val)

        i = len(self.heap) - 1

        # Heapify up
        while i > 0:
            parent = (i - 1) // 2

            if self.heap[parent] <= self.heap[i]:
                break

            self.heap[parent], self.heap[i] = (
                self.heap[i], self.heap[parent]
            )

            i = parent

    # Remove minimum element
    def pop(self):
        if not self.heap:
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        result = self.heap[0]

        # Replace root with last element
        self.heap[0] = self.heap.pop()

        # Heapify down
        i = 0
        n = len(self.heap)

        while True:
            left = 2 * i + 1
            right = 2 * i + 2
            smallest = i

            if left < n and self.heap[left] < self.heap[smallest]:
                smallest = left

            if right < n and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest == i:
                break

            self.heap[i], self.heap[smallest] = (
                self.heap[smallest], self.heap[i]
            )

            i = smallest

        return result

    # Get minimum element
    def peek(self):
        if not self.heap:
            return None

        return self.heap[0]

    def is_empty(self):
        return len(self.heap) == 0


# Example
pq = PriorityQueue()

pq.push(5)
pq.push(3)
pq.push(8)
pq.push(1)
pq.push(4)

print(pq.heap)   # [1, 3, 8, 5, 4]

print(pq.peek()) # 1
print(pq.pop())  # 1
print(pq.pop())  # 3
print(pq.pop())  # 4