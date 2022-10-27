# First attempt

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeLists(l1, l2):

    prehead = ListNode()
    current = prehead

    while l1 and l2:

        if l2.val > l1.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next

        current = current.next

    current.next = l1 if l1 else l2

    return prehead.next


# The idea behind this recursive function is, given the two input nodes, return
# the smallest value back up the recursion stack...
def mergeListRecur(l1, l2):

    # Check if either of the input is null input.
    # If l1 is null, return l2 since no sorting is required
    if l1 is None:
        return l2
    # Same goes for l2. Return l1 as there is no sorting to be done:
    if l2 is None:
        return l1

    # Once we determined both inputs were a LinkedList node, we compare their values.
    if l1.val < l2.val:
        l1.next = mergeListRecur(l1.next, l2)
        return l1
    else:
        l2.next = mergeListRecur(l1, l2.next)
        return l2
