# This algoritm compare two string and return "true" if they are anagrams and "false" if they are not.
# I created two hashmaps to store the characters as the key and number of occurrences as the value. 
# Then i compare if the two hash maps are equal or not.

# Time: O(n)
# Memory: O(n)

firstWord = "anagram"
secondWord = "margana"

def validAnagram(word1, word2):
    if len(word1) != len(word2):
        return False
    
    count1, count2 = {}, {}

    for i in range(len(word1)):
        count1[word1[i]] = 1 + count1.get(word1[i], 0)
        count2[word2[i]] = 1 + count2.get(word2[i], 0)
    for c in count1:
        if count1[c] != count2.get(c, 0):
            return False
    return True

result1 = validAnagram(firstWord, secondWord)
print(result1)