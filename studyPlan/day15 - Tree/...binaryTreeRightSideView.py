# Using a breath first search, we traverse through the graph and process nodes
# on each level. By keeping track of all nodes in a level, and maintaining the
# order (left to right), we can record the node values using the same variable,
# where by the time we are processing the last node, we are left with the value
# of the node that is positioned at the very right side of the tree at that
# current level...
