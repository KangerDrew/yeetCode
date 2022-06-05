def numIslands(grid):
    travelled = set()
    island_count = 0

    rows, columns = len(grid), len(grid[0])

    def dfs(row, column):
        if (row, column) in travelled:
            return False

        travelled.add((row, column))

        directions = [[row - 1, column], [row + 1, column], [row, column + 1], [row, column - 1]]

        for r_step, c_step in directions:

            if (r_step in range(rows) and
                    c_step in range(columns) and
                    grid[r_step][c_step] == "1"):
                dfs(r_step, c_step)

        return True

    for r in range(rows):

        for c in range(columns):

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
]
print(numIslands(sample2))
