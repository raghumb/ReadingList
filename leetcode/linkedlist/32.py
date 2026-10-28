# Reverse a linked list - 32


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head):
    prev = None
    curr = head

    while curr:
        next_node = curr.next  # Save the next node
        curr.next = prev      # Reverse the link
        prev = curr            # Move prev forward
        curr = next_node       # Move curr forward

    return prev


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

head = create_linked_list(arr)

print("Original linked list:")
print_linked_list(head)

head = reverse_list(head)

print("Reversed linked list:")
print_linked_list(head)
