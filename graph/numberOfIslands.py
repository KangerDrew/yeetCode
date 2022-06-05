import collections


def numIslands(grid):
    travelled = set()
    island_count = 0

    rows, columns = len(grid), len(grid[0])

    # Although we can use bfs, dfs is easier to write:
    def dfs(row, column):
        # Check if we've already travelled to this section:
        if (row, column) in travelled:
            # We won't utilize return statement value, but use it
            # purely as exit condition.
            return None

        # If it hasn't been travelled, add to travelled hash set:
        travelled.add((row, column))

        # Cleaner than calling dfs 4 times. Use for loop instead:
        directions = [[row - 1, column], [row + 1, column], [row, column + 1], [row, column - 1]]

        for r_step, c_step in directions:

            # First, check r_step and c_step are in bounds,
            # then confirm that those spots are "1" (land)
            if (r_step in range(rows) and
                    c_step in range(columns) and
                    grid[r_step][c_step] == "1"):
                dfs(r_step, c_step)

        # We will not utilize the returned True value...
        return True

    def bfs(row, column):

        # Use python's deque DS, which is a specialized list
        # that has O(1) operation for removing/adding items
        #  to beginning & end of it.
        queue = collections.deque()
        queue.append([row, column])
        # Mark down (row, column) as travelled:
        travelled.add((row, column))

        while queue:

            # .popleft() gets the first item on deque:
            current_r, current_c = queue.popleft()

            # Same as dfs before...
            directions = [[current_r - 1, current_c], [current_r + 1, current_c],
                          [current_r, current_c + 1], [current_r, current_c - 1]]

            for r_step, c_step in directions:

                # Check r_step and c_step are in bounds, then confirm
                # that those spots are "1" (land).
                # NEW FOR BFS - AND make sure that it has not been
                # travelled already:
                if (r_step in range(rows) and
                        c_step in range(columns) and
                        grid[r_step][c_step] == "1" and
                        (r_step, c_step) not in travelled):
                    # Append the un-travelled r_step, c_step to queue:
                    queue.append([r_step, c_step])
                    # Mark down (r_step, c_step) as travelled:
                    travelled.add((r_step, c_step))

        return None

    for r in range(rows):

        for c in range(columns):

            # When we hit a piece of unexplored island, we perform
            # either dfs or bfs, and increment the count by 1.

            # Performing dfs/bfs will add other "1"s attached
            # to grid[r][c] to the travelled set. This means
            # the same island will not be counted more than twice!
            if grid[r][c] == "1" and (r, c) not in travelled:
                bfs(r, c)
                island_count += 1

    return island_count


sample1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]  # should return 1

# print(numIslands(sample1))

sample2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]  # should return 3
# print(numIslands(sample2))

sample3 = [
    ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "0", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "0"],
    ["1", "0", "1", "1", "1", "0", "0", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "0", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1"],
    ["1", "0", "1", "1", "1", "1", "1", "0", "1", "1", "1", "0", "1", "1", "1", "1", "0", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "1", "1", "0"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "0", "1", "1", "1", "1", "0", "0"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"],
    ["1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1", "1"]
]  # should return 1
print(numIslands(sample3))


sample4 = [
    ["1", "1", "1"],
    ["0", "1", "1"],
    ["1", "0", "1"]
]  # should return 2

