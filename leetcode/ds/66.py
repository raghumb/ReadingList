# queue from scratch

class Queue:
    def __init__(self):
        self.queue = []

    # Add element at rear
    def enqueue(self, val):
        self.queue.append(val)

    # Remove element from front
    def dequeue(self):
        if self.is_empty():
            return None

        return self.queue.pop(0)

    # Return front element without removing
    def peek(self):
        if self.is_empty():
            return None

        return self.queue[0]

    # Check whether queue is empty
    def is_empty(self):
        return len(self.queue) == 0

    # Return number of elements
    def size(self):
        return len(self.queue)


# Example
queue = Queue()

queue.enqueue(10)
queue.enqueue(20)
queue.enqueue(30)

print(queue.queue)      # [10, 20, 30]
print(queue.peek())     # 10
print(queue.dequeue())  # 10
print(queue.dequeue())  # 20
print(queue.peek())     # 30
print(queue.size())     # 1
print(queue.is_empty()) # False