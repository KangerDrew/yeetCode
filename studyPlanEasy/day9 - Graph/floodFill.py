import collections
# My first attempt:

def floodFill(image, sr, sc, color):

    starting = image[sr][sc]

    # Infinite loop prevention - if the color is exactly the same as the starting position,
    # we don't need to go into dfs traversal to change all the colors in the image (nothing
    # to change in the first place). We need to return back the original input, otherwise
    # we'll end up with stack overflow!!
    if starting == color:
        return image

    def dfs(r, c):

        # This if statement wouldn't work if starting == color:
        if image[r][c] == starting:
            image[r][c] = color

            directions = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]

            for new_r, new_c in directions:
                if 0 <= new_r < len(image) and 0 <= new_c < len(image[0]):
                    dfs(new_r, new_c)

        return None

    dfs(sr, sc)
    return image


# Also solved it using iterative BFS (faster in python because python sucks at recursion):
def floodFillBFS(image, sr, sc, color):

    starting = image[sr][sc]

    # Infinite loop prevention - if the color is exactly the same as the starting position,
    # we don't need to go into bfs traversal to change all the colors in the image (nothing
    # to change in the first place). We need to return back the original input, otherwise
    # we'll end up with infinite loop!
    if starting == color:
        return image

    queue = collections.deque([(sr, sc)])

    while queue:
        r, c = queue.popleft()

        # This if statement wouldn't have worked if color == starting:
        if image[r][c] == starting:

            image[r][c] = color
            directions = [(r - 1, c), (r + 1, c), (r, c + 1), (r, c - 1)]

            for new_r, new_c in directions:
                if 0 <= new_r < len(image) and 0 <= new_c < len(image[0]):
                    queue.append((new_r, new_c))

    return image
