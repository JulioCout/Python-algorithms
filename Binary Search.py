# Given an array of integers nums which is sorted in ascending order, and an integer target, write a function to search target in nums.
# If target exists, then return its index. Otherwise, return -1.

# O(log₂ n)

nums = [-1,0,3,5,9,12]
target = 11

def binary_search(nums, target):
    l, r = 0, len(nums) -1

    while l <= r:
        m = (l + r) // 2
        if nums[m] < target:
            l = m + 1
        elif nums[m] > target:
            r = m - 1
        else:
            return m
    return -1
    
    
result = binary_search(nums, target)
print(result)
