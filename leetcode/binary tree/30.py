# K'th Largest Element in BST

# Given the root of a Binary Search Tree (BST) and an integer k, 
# find the k-th largest element in the BST without modifying its structure.


# A BST is a binary tree that follows an ordering rule:
# - Left subtree: values are smaller than the node.
# - Right subtree: values are greater than the node.
# - The same rule applies recursively to every node.
# inorder gives ascending order, while reverse inorder gives descending order.

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


def insert(root, val):
    if root is None:
        return TreeNode(val)

    if val < root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)

    return root


def kth_largest(root, k):
    count = 0
    result = None

    def reverse_inorder(node):
        nonlocal count, result

        if node is None or result is not None:
            return

        reverse_inorder(node.right)

        count += 1
        if count == k:
            result = node.val
            return

        reverse_inorder(node.left)

    reverse_inorder(root)
    return result


# Input values to construct the BST
values = list(map(int, input("Enter BST values: ").split()))

root = None
for val in values:
    root = insert(root, val)

k = int(input("Enter k: "))

if k <= 0 or k > len(values):
    print("Invalid k")
else:
    print("K-th largest element:", kth_largest(root, k))