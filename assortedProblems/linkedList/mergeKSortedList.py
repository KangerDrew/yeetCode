# This is a harder variant of merge two sorted list problem.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists):

    # This is a solution for the easier variant problem:
    def mergeList(l1, l2):
        dummy = ListNode()
        tail = dummy

        while l1 and l2:
            if l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        if l1:
            tail.next = l1

        if l2:
            tail.next = l2

        return dummy.next

    # Here is where the real function begins:

    # Edge case, where we are given an empty "lists"
    if not lists or len(lists) == 0:
        return None

    # We will use while loop to repeatedly perform merge two lists
    # at a time, until only 1 remains:
    while len(lists) > 1:
        # create a new array that will contain an updated lists:
        mergedLists = []

        # Loop through the original lists, but increment by 2:
        for i in range(0, len(lists), 2):
            # Get node 1 and node 2:
            l1 = lists[i]
            # node 2 may not exist, if i + 1 is out of bounds:
            l2 = lists[i + 1] if i + 1 < len(lists) else None

            # Use mergeList helper function to merge l1 and l2, and
            # append it to the mergedLists array:
            mergedLists.append(mergeList(l1, l2))

        # Replace lists with updated mergedLists object
        lists = mergedLists

    # There should only be one list remaining in the lists after
    # the while loop. Return it:
    return lists[0]
