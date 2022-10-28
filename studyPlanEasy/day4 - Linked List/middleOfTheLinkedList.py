# First attempt:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def linkedListMiddle(head):

    p1, p2 = head, head

    while p2 and p2.next:

        p1 = p1.next
        p2 = p2.next.next

    return p1
