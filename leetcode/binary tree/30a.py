# without nested function , uses stack and iteration

def kth_largest(root, k):
    stack = []
    curr = root
    count = 0

    while curr or stack:
        # Go to the rightmost (largest) node
        while curr:
            stack.append(curr)
            curr = curr.right

        # Process the node
        curr = stack.pop()
        count += 1

        if count == k:
            return curr.val

        # Move to the left subtree
        curr = curr.left

    return None