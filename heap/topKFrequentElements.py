from collections import Counter, defaultdict
import heapq

# IMPORTANT: In questions where we are looking for a top k elements
# that satisfy a certain condition, it is often a good idea to think about
# using heaps!


# The idea is to use min-heap to store the frequency of the integer. By keeping
# the size of the heap as k, the min-heap will keep track of the k most frequent
# counts.

test = [1, 1, 1, 2, 2, 3]
test_count = Counter(test)
print(test_count)
print(test_count[69])
print(test_count)

other_count = defaultdict(int)
other_count["a"] += 1
other_count["b"] += 4
print(other_count)
print(other_count["g"])
print(other_count)

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

