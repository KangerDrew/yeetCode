# Easy problem... but I was stumped...


# The key to solving this problem is knowing that this is
# a Binary S.E.A.R.C.H Tree! Meaning all left node values are
# always less than current value, and all right node values
# are greater than current value!!
def lowestCommonAncestor(root, p, q):

    # Set pointer to current root node:
    current = root

    while current:
        # If both p and q values are greater than current
        # value, lowest common ancestor must reside somewhere
        # in the right:
        if p.val > current.val and q.val > current.val:
            current = current.right
        # If both p and q values are less than current
        # value, lowest common ancestor must reside somewhere
        # in the left:
        elif p.val < current.val and q.val < current.val:
            current = current.left
        # If neither if statements were triggered, there are two
        # possible scenarios - both indicating we've reached the
        # lowest common ancestor:

        # Scenario 1: One of the value is greater than current.val,
        # and other is less than current.val. This means that there
        # is a split, and we cannot take either the left or right
        # because that would exclude one of the node.

        # Scenario 2: One of the value is equal to the current.val,
        # which means that current value is the lowest possible
        # common ancestor (can't go any lower since doing so will
        # exclude the current node)
        else:
            return current

    # The function will not require a return statement, assuming
    # the input was a valid BST.

