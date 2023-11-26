# If the list is sorted first, I can compare two neighboring elements at the same time and can do the check with O(n log n) time efficiency.
# But if I create a hashset to store the elements I have already checked and compare each new element with those in the hashset,
# Whith this solution i'll decrease space efficiency in exchange for O(n) time efficiency.


# Time: O(n)
# Space: O(n)


numberList = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]

def containsDuplicate(nums) -> bool:
        alreadyChecked = set()

        for n in nums:
            if n in alreadyChecked:
                 return True
            alreadyChecked.add(n)
        return False

result = containsDuplicate(numberList)
print(result)