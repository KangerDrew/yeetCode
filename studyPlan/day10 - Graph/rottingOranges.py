import collections

def rottingOranges(grid):

    queue = collections.deque()
    time, fresh = 0, 0
    row, col = len(grid), len(grid[0])

    # loop through the grid, count how many oranges are "fresh"
    # and also add the rotten oranges to the queue:

    for i in range(row):
        for j in range(col):

            # Fresh orange:
            if grid[i][j] == 1:
                fresh += 1
            # Rotten orange, add to queue:
            elif grid[i][j] == 2:
                queue.append((i, j))

    # The queue should be loaded with the rotten oranges. Use bfs to traverse these
    # positions. We ALSO need to stop iterating once it is discovered that all fresh
    # oranges have been eliminated (otherwise we might overestimate the time elapsed):
    while queue and fresh > 0:

        # We need to traverse ALL the nodes present in the queue.
        # This way we simulate bfs traversal beginning at all rotten
        # oranges simultaneously:
        for n in range(len(queue)):
            current = queue.popleft()

            r, c = current
            directions = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]

            # Check 4 directions, see if they can be added to the queue:
            for r, c in directions:
                if (0 <= r < row) and (0 <= c < col) and (grid[r][c] == 1):
                    # Fresh orange is now getting rotten:
                    fresh -= 1
                    grid[r][c] = 2
                    # Add the new rotten orange to the queue:
                    queue.append((r, c))

        # All the rotten oranges should now have spread to all 4 directions.
        # Increment time by 1:
        time += 1

    # Return time elapsed, but only if there are no fresh oranges remaining. Otherwise
    # return -1:
    return time if fresh == 0 else -1

