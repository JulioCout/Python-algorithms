# A very efficiency solution for "Top K Frequent Elements" algoritm.
# Creating a dictionary where the key is the number of occurrence and the value is the list of elements that occur that number of time, i guarantee that the dictionary will not be too big.
# The size of the dictionary will be the size of elements in the list i have to check. Because the number max an element can occur is the size of the list.


# Time: O(n).
# Memory: O(n).


listofNumbers = [1,1,1,2,2,3]
k = 2

def topKFrequent(numbers, k):

    # A dictionary where the key is the frequency of an element and the value is the list of elements that occur that number of times.
    count = {}
    freq = [[] for i in range(len(numbers) + 1)]

    # Counting the number of times it element occurs.
    for n in numbers:
        count[n] = 1 + count.get(n, 0)
    for n, c in count.items():
        freq[c].append(n)

    # Result output
    result = []
    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            result.append(n)
            if len(result) == k:
                return result
            
result = topKFrequent(listofNumbers, k)
print(result)