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

    # Write a dfs traversal algorithm, that checks which nodes will be able
    # to reach the current node we've entered. This means, checking neighboring
    # nodes to see if their height value is greater than or equal to the current
    # node... Make sure to also pass down the correct set depending on which
    # ocean you begin your traversal from:
    def dfs(position, ocean_set):

        if position in ocean_set:
            return None

        ocean_set.add(position)

        r, c = position[0], position[1]
        cur_height = heights[r][c]
        directions = [(r + 1, c), (r - 1, c), (r, c + 1), (r + 1, c - 1)]

        for new_r, new_c in directions:
            if 0 <= new_r < row and 0 <= new_c < col and cur_height <= heights[new_r][new_c]:
                dfs((new_r, new_c), ocean_set)

        return None






