# An algorithm that search throughout an array and group together anagrams.

from collections import defaultdict

strs = ["eat","tea","tan","ate","nat","bat"]

def groupAnagrams(strs):
    anagramMap = defaultdict(list)
    result = []
    
    for word in strs:
        sortedWord = tuple(sorted(word))
        anagramMap[sortedWord].append(word)
    
    for value in anagramMap.values():
        result.append(value)        
    
    return result

result = groupAnagrams(strs)
print(result)