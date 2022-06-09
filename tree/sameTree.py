# My first attempt solution - Recursive:
def isSameTree(p, q):
    if not p and not q:
        return True

    if (not p and q) or (not q and p):
        return False

    if p.val != q.val:
        return False

    if not isSameTree(p.left, q.left) or not isSameTree(p.right, q.right):
        return False

    return True


# We can use either DFS or BFS. It's just a matter of
# simultaneously traversing both nodes at the same time:
def isSameTreeItr(p, q):

    stack = [[p, q]]

    while stack:

        current_p, current_q = stack.pop()

        # If we reach a leaf node without any conflict, skip to the
        # next item on stack:
        if not current_p and not current_q:
            continue

        # If only one of them is None, then we have a mismatch. Return False:
        if (not current_p and current_q) or (not current_q and current_p):
            return False

        # If the values do not match, then we have a mismatch. Return False:
        if current_p.val != current_q.val:
            return False

        # Add left and right node (even if they're none) of p and q, together:
        if current_p or current_q:
            stack.append([current_p.left, current_q.left])
            stack.append([current_p.right, current_q.right])

    # If while loop exited without returning False, it means all nodes matched,
    # so we can return True:
    return True

