# Rotate List

# Given the head of a linked list, rotate the list to the right by k places


class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None


def rotateRight(head, k):

    if not head or not head.next or k == 0:
        return head

    # Step 1: Find length and last node
    length = 1
    tail = head

    while tail.next:
        tail = tail.next
        length += 1

    # Step 2: Handle k greater than length
    k = k % length

    if k == 0:
        return head

    # Step 3: Make the list circular
    tail.next = head

    # Step 4: Find the new tail
    steps = length - k - 1

    new_tail = head

    for _ in range(steps):
        new_tail = new_tail.next

    # Step 5: Set new head and break the circle
    new_head = new_tail.next
    new_tail.next = None

    return new_head


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
head = ListNode(1)
head.next = ListNode(2)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)

k = 2

head = rotateRight(head, k)

# Print result
curr = head

while curr:
    print(curr.val, end=" -> " if curr.next else "\n")
    curr = curr.next
