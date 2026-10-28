# Maximum Depth or Height of a Binary Tree
# The maximum depth or height of the tree is the number of edges in the tree from the root to the deepest node.

# Time O(n), space O(h), h is tree height


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def maxDepth(root):
    if root is None:
        # if depth is number of nodes, instead of edge, then return 0
        return -1

    left_depth = maxDepth(root.left)
    right_depth = maxDepth(root.right)

    return 1 + max(left_depth, right_depth)


# Create this tree:
#        1
#       / \
#      2   3
#     /
#    4

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)

print(maxDepth(root))  # 2

