import heapq
import random


# The easiest solution would be to simply sort the input array,
# and return the kth last element from the array to get the kth
# largest element. Time complexity would be O(n log n). But we
# can do better, using max heap data structure.


# SOLUTION #1 - Using Priority Queue (Min Heap):
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

# JAVA CODE THAT DOES THE SAME THING, WITH LESS ABSTRACTION:
# public int findKthLargest(int[] nums, int k) {
#     // init heap 'the smallest element first'
#     PriorityQueue<Integer> heap =
#         new PriorityQueue<Integer>((n1, n2) -> n1 - n2);
#
#     // keep k largest elements in the heap
#     for (int n: nums) {
#       heap.add(n);
#       if (heap.size() > k)
#         heap.poll();
#     }
#
#     // output
#     return heap.poll();
# }


# SOLUTION #2 - Quick Select Algorithm:

# The concept behind the quick select algorithm is simple. Select a random element
# from an unsorted array, and divide up the array into two partition - One half is
# greater than the random value, and the other half is are less. This will determine
# the "kth" largest position of the randomly selected element. If this randomly
# selected element is less than the specified kth position, we recursively assess
# all elements of the array larger than that value. If it's less, then we assess the
# lower half of the array. If neither, it meant that we've hit the target "kth" value
# so we return that value.

def findKthLargestQuickSelect(nums, k):

    # Get the left and right boundaries
    left, right = 0, len(nums) - 1

    def quickSelect(l, r):

        # First randomly select a pivot element index from nums array:
        rand_i = random.randint(l, r)
        # Then, place the random element at the rightmost index (swap them):
        nums[rand_i], nums[r] = nums[r], nums[rand_i]

        # Get the pivot value
        pivot = nums[r]
        # Define a pointer that will
        pointer = l

        # Loop through the array from l to r - 1:
        for i in range(l, r):

            if nums[i] <= pivot:






