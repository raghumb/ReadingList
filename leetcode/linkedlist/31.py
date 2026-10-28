# Remove Nth Node From End of List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):
    dummy = ListNode(0)
    dummy.next = head
    # we want slow to stop one node before the node we need to delete
    slow = dummy
    fast = dummy

    # Move fast n steps ahead
    for _ in range(n):
        fast = fast.next

    # Move both pointers until fast reaches the last node
    while fast.next:
        slow = slow.next
        fast = fast.next

    # Remove the target node
    slow.next = slow.next.next

    return dummy.next


def create_linked_list(arr):
    dummy = ListNode()
    current = dummy

    for value in arr:
        current.next = ListNode(value)
        current = current.next

    return dummy.next


def print_linked_list(head):
    current = head

    while current:
        print(current.val, end=" -> ")
        current = current.next

    print("None")


# Hardcoded input
arr = [1, 2, 3, 4, 5]
n = 2

# Create linked list
head = create_linked_list(arr)

print("Original linked list:")
print_linked_list(head)

# Remove nth node from the end
head = removeNthFromEnd(head, n)

print("Updated linked list:")
print_linked_list(head)