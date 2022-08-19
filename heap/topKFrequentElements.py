from collections import Counter, defaultdict
import heapq

# IMPORTANT: In questions where we are looking for a top k elements
# that satisfy a certain condition, it is often a good idea to think about
# using heaps!


# The idea is to use min-heap to store the frequency of the integer. By keeping
# the size of the heap as k, the min-heap will keep track of the k most frequent
# counts.

# test = [1, 1, 1, 2, 2, 3]
# test_count = Counter(test)
# print(test_count)
# print(test_count[69])
# print(test_count)
#
# other_count = defaultdict(int)
# other_count["a"] += 1
# other_count["b"] += 4
# print(other_count)
# print(other_count["g"])
# print(other_count.items())

# Solution #1 - Min-Heap:
def topKFrequent(nums, k):
    # O(1) time
    if k == len(nums):
        return nums

    # 1. build hash map : character and how often it appears
    # O(N) time
    count = Counter(nums)
    # 2-3. build heap of top k frequent elements and
    # convert it into an output array
    # O(N log k) time
    return heapq.nlargest(k, count.keys(), key=count.get)


print(topKFrequent([1, 1, 1, 1, 3, 3, 4], 2))

# Using lambda function for ease of explanation. INVALID SOLUTION:
def topKFrequentLambda(nums, k):

    # Edge case:
    if k == len(nums):
        return nums

    # Convert the provided nums array into a counter dictionary
    count = Counter(nums)
    # Convert it to a list of tuples - (number from nums, frequency of that number)
    tuple_count = list(count.items())

    # key in the nlargest function is specifying to retrieve the nlargest value in the
    # provided tuple_count, using the "frequency of that number" value (i.e. index
    # 1 value of the tuple)
    return heapq.nlargest(k, tuple_count, key=lambda a: a[1])


# This returns a list of tuples, with both the numbers and their frequencies:
print(topKFrequentLambda([1, 1, 1, 1, 3, 3, 4], 2))

# Solution #2 - Bucket Sort:
