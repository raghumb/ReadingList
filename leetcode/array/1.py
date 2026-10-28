 # Max Sum Subarray of Size K

def max_sum_subarray_of_size_k(arr, k):
    n = len(arr)
    if n < k:
        return -1
    
    current_sum = sum(arr[:k])
    max_sum = current_sum
    
    for i in range(k, n):
        current_sum += arr[i] - arr[i - k]
        max_sum = max(max_sum, current_sum)
        
    return max_sum

# Example usage:
arr = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
print(max_sum_subarray_of_size_k(arr, k))  # Output: 39