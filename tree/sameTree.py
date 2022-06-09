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

