# Median of 2 sorted arrays
# Given two sorted arrays arr1 and arr2 of size m and n respectively, return the median of the two sorted arrays.

# The median is defined as the middle value of a sorted list of numbers. 
# In case the length of the list is even, the median is the average of the two middle elements.



"""
    select the smaller of the two pointed-to values, then advance that pointer. o(m+n)
    
    """
def find_median(arr1, arr2):
    m = len(arr1)
    n = len(arr2)

    i = 0
    j = 0
    prev = 0
    curr = 0

    for _ in range((m + n) // 2 + 1):
        prev = curr
        
        
        # array 2 has no elements left or arr1 is less than arr2 elmeent
        if i < m and (j >= n or arr1[i] <= arr2[j]):
            curr = arr1[i]
            i += 1
        else:
            curr = arr2[j]
            j += 1

    if (m + n) % 2 == 1:
        return curr

    return (prev + curr) / 2

arr1 = [2, 4, 6]
arr2 = [1, 3, 5]
print(find_median(arr1, arr2))