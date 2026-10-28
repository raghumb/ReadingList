# Find peak element

nums = [1, 2, 1, 3, 5, 6, 4]

left = 0
right = len(nums) - 1

while left < right:

    mid = (left + right) // 2

    if nums[mid] < nums[mid + 1]:
        # Peak must exist on the right
        left = mid + 1
    else:
        # Peak exists at mid or on the left
        right = mid

print(left)