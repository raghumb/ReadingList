# find  intersection of 2 linked list


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def get_intersection_node(headA, headB):
    p1 = headA
    p2 = headB

    while p1 != p2:
        if p1 is None:
            p1 = headB
        else:
            p1 = p1.next

        if p2 is None:
            p2 = headA
        else:
            p2 = p2.next

    return p1


def print_list(head):
    current = head
    while current:
        print(current.val, end=" -> ")
        current = current.next
    print("None")


# List A: 1 -> 2 \
#                   8 -> 9 -> None
# List B: 4 -> 5 /

# Shared nodes
common1 = ListNode(8)
common2 = ListNode(9)
common1.next = common2

# List A
a1 = ListNode(1)
a2 = ListNode(2)
a1.next = a2
a2.next = common1

# List B
b1 = ListNode(4)
b2 = ListNode(5)
b1.next = b2
b2.next = common1

headA = a1
headB = b1

print("List A:")
print_list(headA)

print("List B:")
print_list(headB)

intersection = get_intersection_node(headA, headB)

if intersection:
    print("Intersection found at node:", intersection.val)
else:
    print("No intersection")
