
 # Max Sum Subarray of Size K
def window(arr, size):
    max_sum = 0

    sum = 0
    for i in range(0, size):
        sum += arr[i]
    
    if sum > max_sum:
        max_sum = sum
    
    #init start index
    #init start index
    
    start = size
    end = start + size
    
    #loop condition
        #move end index
        #add end index value
        #subtract start index value
        #move start index
        #other conditions for comparison
        
    while end + 1 < len(arr):
        end = end + 1
        sum += arr[end]
        sum -= arr[start]
        start = start + 1
        
        if sum > max_sum:
            max_sum = sum
            
    return sum

a = [1, 4, 2, 10, 23, 3, 1, 0, 20]
k = 4
sum = window(a, k)
print(sum)
        
        
    
        
    
        
    