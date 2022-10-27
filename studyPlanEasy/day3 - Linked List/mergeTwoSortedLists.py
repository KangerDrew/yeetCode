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

