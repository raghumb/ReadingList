# Given an unsorted integer array nums. Return the smallest positive integer
# that is not present in nums.

# O(n)

"""
    The key observation is:

For an array of length (n), the answer must be between 1 and n+1.

For example, if the array has four elements, the answer must be one of 1, 2, 3, 4, 5.

We can place each positive number \(x\) at index \(x-1\).
After rearranging the array, each index should contain the number index + 1.
    """

nums = [3, 4, -1, 1]

n = len(nums)
i = 0

while i < n:
    correct_index = nums[i] - 1

    # second condition, This prevents an infinite loop when duplicates exist.
    if 1 <= nums[i] <= n and nums[i] != nums[correct_index]:
        nums[i], nums[correct_index] = nums[correct_index], nums[i]
    else:
        i += 1

for i in range(n):
    if nums[i] != i + 1:
        print(i + 1)
        break
else:
    
    # for-else: The else block executes only if the loop finishes normally, without encountering a break.
    print(n + 1)
