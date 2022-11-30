# The diameter is defined by the length of the longest path between any nodes in a tree.
# The easiest approach here is to use a recursive function for the bottom-up style approach,
# where we go all the way to the leaf node and as we come back up, we keep track of the "longest
# path" that we can take on the left side and the right side of the given node. The greatest
# diameter of that current node will be the sum of the longest path of left and right side.

# We need to constantly update what the diameter value is at each node, as greatest diameter won't
# necessarily go through the root node!!

# Once we determine the greatest diameter of the current node, we pass the longest path (either left
# or right) up the level. We do not need to worry about the shorter path as we're only concerned with
# the longest path we can take. We can discard the shorter path once the diameter is calculated and
# compared.
