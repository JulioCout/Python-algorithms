# In this algorithm the objective is to test if the informed string is a palindrome.
# I created a function that compares the reverse of the string with the string itself and returns "true" if they are equal or "false" if they are different.

# Time: O(n)
# Memory: O(1)


def isAlphaNum(c):
    return (ord('A') <= ord(c) <= ord('Z') or
            ord('a') <= ord(c) <= ord('z') or
            ord('0') <= ord(c) <= ord('9'))


textToTest = "teset"

def ValidPalindrome(stringToTest):
    l, r = 0, len(stringToTest) -1

    while l < r:
        while not isAlphaNum(stringToTest[l]):
            l += 1
        while not isAlphaNum(stringToTest[l]):
            r -= 1
        if stringToTest[l].lower() != stringToTest[r].lower():
            return False
        l, r = l + 1, r - 1
    return True




result = ValidPalindrome(textToTest)
print(result)