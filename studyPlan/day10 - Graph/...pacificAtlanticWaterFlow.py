# Use a set to see which nodes are able to reach Pacific Ocean (start dfs from
# the top-left edge, as those are right next to the Pacific Ocean to begin with).
# Then, use another set to check which nodes will reach Atlantic Ocean, starting
# from the bottom-right edge (same logic as before)

# After the traversals are done, we check to see which nodes can BOTH reach the
# Pacific AND Atlantic Ocean by looping through the sets to check which nodes
# are present in both sets.


def waterFlow(heights):

    row, col = len(heights), len(heights[0])
    # Pacific Ocean is top and left, Atlantic Ocean is right and bottom:
    set_pacific, set_atlantic = set(), set()

    # Write a dfs traversal algorithm, that checks which positions will be able
    # to reach the current position we've entered. This means, checking neighboring
    # positions to see if their height value is greater than or equal to the current
    # position... Make sure to also pass down the correct set depending on which
    # ocean you begin your traversal from:
    def dfs(position, ocean_set):

        if position in ocean_set:
            return None

        ocean_set.add(position)

        r, c = position[0], position[1]
        cur_height = heights[r][c]
        directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)]

        for new_r, new_c in directions:
            if 0 <= new_r < row and 0 <= new_c < col and cur_height <= heights[new_r][new_c]:
                dfs((new_r, new_c), ocean_set)

        return None

    # Run dfs() on positions on the top row (pacific ocean)
    # and positions on the bottom row (atlantic ocean)
    for i in range(col):
        dfs((0, i), set_pacific)
        dfs((row - 1, i), set_atlantic)

    # Run dfs() on positions on the left col (pacific ocean)
    # and positions on the right col (atlantic ocean)
    for j in range(row):
        dfs((j, 0), set_pacific)
        dfs((j, col - 1), set_atlantic)

    # Initialize array to contain all the positions that occur both in
    # set_pacific AND set_atlantic:
    res = []

    # Iterate through either of the sets, and check to see if that position
    # also exists in the other set:
    for node in set_pacific:
        if node in set_atlantic:
            # Append the position, but convert the tuples to array:
            res.append([node[0], node[1]])

    return res

