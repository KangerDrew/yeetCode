import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):

        self.minHeap, self.k = nums, k
        # Use heapq's heapify function to convert self.minHeap to min heap:
        heapq.heapify(self.minHeap)
        # Use while loop to remove excess elements. We need our heap size to be k:
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)

    def add(self, val: int) -> int:

        # Push the value into the heap:
        heapq.heappush(self.minHeap, val)

        # Check if the heap length is greater than k. It is possible that
        # the heap was initialized with length less than k!!
        if len(self.minHeap) > self.k:
            # If we exceeded the length k, we pop the smallest element:
            heapq.heappop(self.minHeap)

        # Return the kth largest element, which should be the first element
        # of the minHeap:
        return self.minHeap[0]

