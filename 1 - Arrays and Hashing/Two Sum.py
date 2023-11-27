# In this algorithm the objective is to scroll through a set of data looking for two components that add up will give the result i'm looking for.

# Commonly this type of algorithms use two pointer, one that stay in one element and other that run through the array comparing other elements with the first one.
# But this solution isn't very eficienty, it's O(n²).
# Instead i can use just one pointer that run through the array just one time creating a hashmap and comparing the each next element with the elements in the hashmap.
# With this solution i will have O(n) efficiency.

# Time: O(n)
# Space: O(n)


numbers = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
target_sum = 9


def twoSum(numbers, target_sum):
    alreadyChecked = {} # value : index
    for i, n in enumerate(numbers):
        diff = target_sum - n
        if diff in alreadyChecked:
            return [alreadyChecked[diff], i]
        alreadyChecked[n] = i
    return
                
result = twoSum(numbers, target_sum)
print(result)
