# The difference from this algorithm to the other "two sum" is that in this one the list of numbers is sorted.
# By sorting the list of elements we don't need to run through all the array.
# This solution help to improve the time effincecy.

# Time: O(n)
# Memory: O(n)

listOfNumbers = [1, 3, 4, 5, 7, 11]
targetToFind = 9

def twoSumII(nums, target):
    l, r = 0, len(nums) - 1
    
    while l < r:
        currentSum = nums[l] + nums[r]
        if currentSum < target:
            l += 1
        elif currentSum > target:
            r -= 1
        else:
            return [nums[l], nums[r]]
    return []


result = twoSumII(listOfNumbers, targetToFind)
print(result)