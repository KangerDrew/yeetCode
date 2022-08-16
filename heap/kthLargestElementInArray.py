import heapq


# The easiest solution would be to simply sort the input array,
# and return the kth last element from the array to get the kth
# largest element. Time complexity would be O(n log n). But we
# can do better, using max heap data structure.

# When using heap, we create a min-heap of length k, which will cost
# us O(k). Then, we add the remaining elements one by one, while
# maintaining the length k for the min-heap by popping the smallest
# element each time we add a new element. This operation will cost
# us around O( (n - k) log(k) )

# At the end, we will be left with a heap with a length k, which will
# consist of k largest values in the original list. The smallest of these
# will be the kth largest value of the original list!

# Unfortunately in python, this process is abstracted away from us by
# nlargest function, which returns the sorted n largest values in the
# array from largest to smallest. Thus, returning the last element from
# nlargest gives us the kth largest element from the array...
def findKthLargestHeap(nums, k):

    return heapq.nlargest(k, nums)[-1]


print(findKthLargestHeap([3, 2, 1, 5, 6, 4], 2))

