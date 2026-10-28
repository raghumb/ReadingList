# Search in rotated sorted array

"""
    Given an integer array arr, sorted in ascending order (with distinct values) and a target value k. The array is rotated at some pivot point that is unknown. 
    Find the index at which k is present and if k is not present return -1.
    """
    
# Binary Search in (O(log n))


def search(arr, k):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2
        
        if arr[left] == k:
            return left
        
        if arr[right] == k:
            return right

        if arr[mid] == k:
            return mid

        # Left half is sorted
        if arr[left] <= arr[mid]:
            if arr[left] < k < arr[mid]:
                right = mid - 1
            else:
                left = mid + 1

        # Right half is sorted
        else:
            if arr[mid] < k < arr[right]:
                left = mid + 1
            else:
                right = mid - 1

    return -1


print(search([4, 5, 6, 7, 0, 1, 2], 0))  # 4
print(search([4, 5, 6, 7, 0, 1, 2], 3))  # -1
print(search([6, 7, 1, 2, 3, 4, 5], 4))  # 5
