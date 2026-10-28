# Find minimum in Rotated Sorted Array


def findMin(arr):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = (left + right) // 2

        # compare the middle element with the rightmost element to determine which 
        # half contains the rotation point.
        if arr[mid] > arr[right]:
            left = mid + 1
        else:
            right = mid

    return arr[left]


print(findMin([3, 4, 5, 1, 2]))       # 1
print(findMin([4, 5, 6, 7, 0, 1, 2])) # 0
print(findMin([2, 3, 4, 5, 1]))       # 1

