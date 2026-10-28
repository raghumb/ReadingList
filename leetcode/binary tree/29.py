# Sorted Array to Balanced BST


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def sortedArrayToBST(nums):
    if not nums:
        return None

    mid = len(nums) // 2

    root = TreeNode(nums[mid])

    root.left = sortedArrayToBST(nums[:mid])
    root.right = sortedArrayToBST(nums[mid + 1:])

    return root


# Sorted array
nums = [-10, -3, 0, 5, 9]

root = sortedArrayToBST(nums)

# Root = 0
print(root.val)        # 0
print(root.left.val)   # -3
print(root.right.val)  # 9


