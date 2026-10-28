# Check if Symmetric Tree
# Given the root of a binary tree, determine whether it is symmetric around root,
# i.e., check if the binary tree is a mirror image of itself.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isMirror(left, right):
    if left is None and right is None:
        return True

    if left is None or right is None:
        return False

    return (
        left.val == right.val
        and isMirror(left.left, right.right)
        and isMirror(left.right, right.left)
    )

def isSymmetric(root):
    if root is None:
        return True

    return isMirror(root.left, root.right)


# Symmetric tree:
#       1
#      / \
#     2   2
#    / \ / \
#   3  4 4  3

root = TreeNode(
    1,
    TreeNode(2, TreeNode(3), TreeNode(4)),
    TreeNode(2, TreeNode(4), TreeNode(3))
)

print(isSymmetric(root))  # True
