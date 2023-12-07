# Return the length of the longest consecutive elements sequence.

# Time: O(n)
# Memory: O(n)

numbers = [0,3,7,2,5,8,4,6,0,1]

def longestConsecutive(nums):
      numsToCheck = set(nums)
      longest = 0
    
      for n in numsToCheck:
          if (n - 1) not in numsToCheck:
              length = 0
              while (n + length) in numsToCheck:
                  length += 1
              longest = max(length, longest)
      return longest

result = longestConsecutive(numbers)
print(result)