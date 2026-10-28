# check if Children Sum in a Binary Tree

"""
    Given a binary tree, find if it satisfies the Children Sum Property which has the following rules

Each non-leaf node must have a value equal to the sum of its left and right children's values.
A NULL child is considered to have a value of 0, and all leaf nodes are considered valid by default.
    """
    

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def childrenSum(root):
    if root is None:
        return True

    # Leaf nodes are always valid
    if root.left is None and root.right is None:
        return True

    left_val = root.left.val if root.left else 0
    right_val = root.right.val if root.right else 0

    if root.val != left_val + right_val:
        return False

    return childrenSum(root.left) and childrenSum(root.right)


# Valid tree:
#       10
#      /  \
#     4    6
#    / \
#   2   2

root = TreeNode(
    10,
    TreeNode(4, TreeNode(2), TreeNode(2)),
    TreeNode(6)
)

print(childrenSum(root))  # True
