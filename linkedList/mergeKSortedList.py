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

    while len(lists) > 1:
        mergedLists = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None

            mergedLists.append(mergeList(l1, l2))

        lists = mergedLists

    return lists[0]
