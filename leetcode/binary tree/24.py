# Check if Two Trees are Identical
#  Two trees are identical when they have the same data and the arrangement of the data is also same.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isSameTree(p, q):
    # Both nodes are empty
    if p is None and q is None:
        return True

    # Only one node is empty
    if p is None or q is None:
        return False

    # Values must match, and both subtrees must match
    return (
        p.val == q.val
        and isSameTree(p.left, q.left)
        and isSameTree(p.right, q.right)
    )


# Tree 1:       1
#              / \
#             2   3

p = TreeNode(1, TreeNode(2), TreeNode(3))

# Tree 2:       1
#              / \
#             2   3

q = TreeNode(1, TreeNode(2), TreeNode(3))

print(isSameTree(p, q))  # True
