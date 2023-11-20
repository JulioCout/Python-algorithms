# In this algorithm the objective is to test if the informed string is a palindrome.
# I created a function that compares the reverse of the string with the string itself and returns "true" if they are equal or "false" if they are different.
#


word = "teset"

def solution(string):
    return string == string[::-1]
    
result = solution(word)
print(result)