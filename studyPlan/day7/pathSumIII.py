# The approach for this problem is to use a HashMap that keeps track of
# "the prefix sum". The prefix sum in binary tree is the list of continuous
# sum from the root to the leaf node, where at each new level you keep track
# of what the current total sum of the nodes traversed are.

# At each level, we'll keep track of what the currentSum value is, and record
# how many times that currentSum value has occurred during that traversal,
# using a HashMap.

# The prefix sum list (we'll be using dictionary to keep track of this) will
# allow us to check for two following scenarios:

# Scenario 1) The targetSum is reached by summing all the traversed nodes
# Scenario 2) The targetSum CAN be reached, if we remove some nodes at the
# beginning of the summed nodes.

# Scenario 1 is easy enough to determine as we traverse down the tree. For
# scenario 2 however, we can check by subtracting the currentSum from the
# targetSum value, and see if that leftover value was recorded during the
# traversal...


