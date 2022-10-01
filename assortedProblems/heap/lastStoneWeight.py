import heapq


def lastStoneWeight(stones):
    # Python's heapq library utilizes min-heap, so we
    # must convert all integers in stones array to negative
    # so we get the behavior of max-heap instead!
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        # Pop the two "largest" (largest negative values) from the heap:
        stone_1 = heapq.heappop(stones)
        stone_2 = heapq.heappop(stones)

        # If two values are different, push the negative abs of the difference
        # into the heap. Otherwise the two stones are destroyed:
        if stone_1 != stone_2:
            heapq.heappush(stones, abs(stone_1 - stone_2) * -1)

    # Return the only remaining stone in the list, or zero
    # if there are no stones remaining in the list:
    return -stones[0] if len(stones) > 0 else 0
