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
    def dfs(node, cur_height, ocean_set):

        if node in ocean_set:
            return

        ocean_set.add(node)



