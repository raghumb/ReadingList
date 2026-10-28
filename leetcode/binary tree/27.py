# Check if Balanced Binary Tree or Not
# Given the root of a binary tree, determine if it is height-balanced or not.

# Note: A binary tree is considered height-balanced if the absolute difference 
# in heights of the left and right subtrees is at most 1 for every node in the tree.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def isBalanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) > 1:
        return False

    return isBalanced(root.left) and isBalanced(root.right)


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


# Balanced tree:
#       1
#      / \
#     2   3
#    /
#   4

root = TreeNode(
    1,
    TreeNode(2, TreeNode(4)),
    TreeNode(3),
)

print(isBalanced(root))  # True
