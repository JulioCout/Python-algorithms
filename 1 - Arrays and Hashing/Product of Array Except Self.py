# This algorithm traverse the array, find the product of each element except the current element,
# and store it in the output array.

# Time: O(n)
# Memory: O(1)

numbers = [1, 2, 3, 4]

def productExceptSelf(nums):
    result = [] * (len(nums))

    prefix = 1
    for n in range(len(nums)):
        result[n] = prefix
        prefix *= nums[n]

    postfix = 1
    for n in range(len(nums) - 1, -1, -1):
        result[n] *= postfix
        postfix *= nums[n]

    return result

result = productExceptSelf(numbers)
print(result)
