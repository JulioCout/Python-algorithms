# In this algorithm the objective is to scroll through a set of data looking for two components that add up will give the result we are looking for.
# I created a function that receives as parameters two variables, one with the data and one that have the target we are looking for.
# The function will browse the array with two pointers, comparing two elements at time until it find two elements compatible to the objective.
# Finally, it will return the two elements.


numbers = [4, 1, 2, -2, 11, 15, 1, -1, -6, -4]
target_sum = 9


def solution(numbers, target_sum):
    for numberIndexA in range(len(numbers)):
        numberA = numbers[numberIndexA]
        for numberIndexB in range(numberIndexA + 1, len(numbers)):
            if numberA + numbers[numberIndexB] == target_sum:
                return [numberA, numbers[numberIndexB]]
    return []
                
result = solution(numbers, target_sum)
print(result)