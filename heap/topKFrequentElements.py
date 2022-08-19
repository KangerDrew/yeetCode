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
# This solution runs in O(n log (k) ) time, since we create a heap of size k
# and we perform push-pop operation n times to keep only the integers with highest
# frequency

# The space complexity is O(n + k), where n would be the max size of a hash map we
# create to keep the frequency, and k is the size of the min-heap.
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
def topKFrequentBucket(nums, k):

    count = {}
    freq = [[] for i in range(len(nums) + 1)]

    for n in nums:
        count[n] = 1 + count.get(n, 0)

    for n, c in count.items():
        freq[c].append(n)

    res = []

    for i in range(len(freq) - 1, 0, -1):
        for n in freq[i]:
            res.append(n)
            if len(res) == k:
                return res