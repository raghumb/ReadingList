# Invert Binary Tree - Change to Mirror Tree


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def invertTree(root):
    if root is None:
        return None

    # Swap left and right children
    # Python evaluates the right-hand side first, so both original child references are preserved before assignment.
    # otherwise, use a temp variable for multi line assignment
    root.left, root.right = root.right, root.left

    # Invert both subtrees
    invertTree(root.left)
    invertTree(root.right)

    return root


# Create tree:
#       1
#      / \
#     2   3
#    / \
#   4   5

root = TreeNode(
    1,
    TreeNode(2, TreeNode(4), TreeNode(5)),
    TreeNode(3)
)

invertTree(root)

# Result:
#       1
#      / \
#     3   2
#        / \
#       5   4
