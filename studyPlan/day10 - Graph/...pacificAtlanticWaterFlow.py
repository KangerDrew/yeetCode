# Use a set to see which nodes are able to reach Pacific Ocean (start dfs from
# the top-left edge, as those are right next to the Pacific Ocean to begin with).
# Then, use another set to check which nodes will reach Atlantic Ocean, starting
# from the bottom-right edge (same logic as before)

# After the traversals are done, we check to see which nodes can BOTH reach the
# Pacific AND Atlantic Ocean by looping through the sets to check which nodes
# are present in both sets.
