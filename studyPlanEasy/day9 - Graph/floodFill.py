import collections
# My first attempt:

def floodFill(image, sr, sc, color):

    starting = image[sr][sc]

    def dfs(r, c):
        if image[r][c] == color:
            return None

        if image[r][c] == starting:
            image[r][c] = color

            directions = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]

            for new_r, new_c in directions:
                if 0 <= new_r < len(image) and 0 <= new_c < len(image[0]):
                    dfs(new_r, new_c)

        return None

    dfs(sr, sc)
    return image


# Also solved it using BFS (faster in python because python sucks at recursion):
def floodFillBFS(image, sr, sc, color):
    starting = image[sr][sc]
    queue = collections.deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()

        if image[r][c] == color:
            continue

        if image[r][c] == starting:

            image[r][c] = color
            directions = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]

            for new_r, new_c in directions:
                if 0 <= new_r < len(image) and 0 <= new_c < len(image[0]):
                    queue.append((new_r, new_c))

    return image
