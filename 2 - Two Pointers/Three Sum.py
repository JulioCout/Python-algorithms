# Finding three elements in the array that when summed the result is 0.

# Time: O(n²)
# Memory: O(1) || O(n) depending on the sorting method.

listToCheck = [-1,0,1,2,-1,-4]

def threeSum(numbers):
    res = []
    numbers.sort()

    for i, a in enumerate(numbers):

        # is duplicated?
        if i > 0 and a == numbers[i - 1]:
            continue

        # left and right pointer
        l, r = i + 1, len(numbers) - 1

        # Moving pointers and making test
        while l < r:
            threeSumResult = a + numbers[l] + numbers[r]
            if threeSumResult > 0:
                r -= 1
            elif threeSumResult < 0:
                l += 1
            else:
                res.append([a, numbers[l], numbers[r]])
                while numbers[l] == numbers[l - 1] and l < r:
                    l += 1
    return res

result = threeSum(listToCheck)
print(result)