# My first blind attempt:

def maxAreaOfIsland(grid):
    travelled = set()
    row, column = len(grid), len(grid[0])
    largest = 0

    def dfs(r, c):

        if (r, c) in travelled or grid[r][c] != 1:
            return 0

        travelled.add((r, c))

        area = 1
        directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for d_r, d_c in directions:

            if d_r in range(row) and d_c in range(column):
                area += dfs(d_r, d_c)

        return area

    for i in range(row):
        for j in range(column):

            if grid[i][j] == 1:
                largest = max(dfs(i, j), largest)

    return largest


print(maxAreaOfIsland([[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
                       [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
                       [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
                      ))
