# My first approach was to use hash set, where we'd store all the
# nodes of one of the list and then iterate through the second list
#  and check to see if the node already exists in the hash set:


def intersectionHashSet(headA, headB):

    stored = set()

    while headA:

        stored.add(headA)
        headA = headA.next

    while headB:

        if headB in stored:
            return headB

        headB = headB.next

    return None


# There is a way to solve this problem without using hash set (O(1) memory)
# It involves the use of two pointers...
