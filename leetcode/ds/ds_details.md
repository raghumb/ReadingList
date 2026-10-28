# Min heap

- Push → Heapify Up: Insert at the end, then move upward until the parent is smaller.
- Pop → Heapify Down: Remove the root, replace it with the last element, then move downward until both children are larger.

- A min heap is a complete binary tree where every parent is smaller than or equal to its children.

## Three formulas to memorize
For a node at index i:
```
parent = (i - 1) // 2
left = 2 * i + 1
right = 2 * i + 2

```

# Priority queue

The difference is conceptual:
- Min Heap: A data structure that maintains the smallest element at the root.
- Priority Queue: A data structure that removes elements according to priority rather than insertion order.

Code is exactly same.

# Max heap
Comparisions change

Min-priority queue	            |  Max-priority queue
Parent ≤ child	                |  Parent ≥ child
Root is minimum	                |  Root is maximum
Heapify up when child is smaller|  Heapify up when child is larger
Heapify down with smaller child	|  Heapify down with larger child

```
# Max priority queue
if self.heap[parent] >= self.heap[i]:
    break

```