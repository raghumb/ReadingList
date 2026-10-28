# check if the linked list has a cycle in it.


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def has_cycle(head):
    slow = head
    fast = head


    """

   Even if the nodes are far apart, the fast pointer moves twice as quickly as the slow pointer, 
   so it eventually catches up with the slow pointer if a cycle exists.
    """
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False


# Create linked list: 1 -> 2 -> 3 -> 4 -> 5
node1 = ListNode(1)
node2 = ListNode(2)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)

node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5

# Create a cycle: 5 -> 3
node5.next = node3

head = node1

if has_cycle(head):
    print("Cycle detected")
else:
    print("No cycle")
