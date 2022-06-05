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

    for r in range(rows):

        for c in range(columns):

            # When we hit a piece of unexplored island, we perform
            # either dfs or bfs, and increment the count by 1.

            # Performing dfs/bfs will add other "1"s attached
            # to grid[r][c] to the travelled set. This means
            # the same island will not be counted more than twice!
            if grid[r][c] == "1" and (r, c) not in travelled:
                dfs(r, c)
                island_count += 1

    return island_count


sample1 = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]  # should return 1

print(numIslands(sample1))

sample2 = [
    ["1", "1", "0", "0", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "1", "0", "0"],
    ["0", "0", "0", "1", "1"]
]  # should return 3
print(numIslands(sample2))
