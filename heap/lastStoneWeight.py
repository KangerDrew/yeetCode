import heapq


def lastStoneWeight(stones):
    # Python's heapq library utilizes min-heap, so we
    # must convert all integers in stones array to negative
    # so we get the behavior of max-heap instead!
    stones = [-s for s in stones]
    heapq.heapify(stones)

    while len(stones) > 1:
        stone_1 = heapq.heappop(stones)
        stone_2 = heapq.heappop(stones)

        if stone_1 != stone_2:
            heapq.heappush(stones, abs(stone_1 - stone_2) * -1)

    return -stones[0] if len(stones) > 0 else 0
