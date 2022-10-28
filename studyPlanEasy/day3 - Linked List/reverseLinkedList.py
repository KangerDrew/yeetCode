# Classic problem. Solve it both iteratively and recursively:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedListItr(head):
    if not head.next:
        return head

    pre = None
    current = head
    post = head.next

    while post:
        current.next = pre
        pre = current
        current = post
        post = post.next

    current.next = pre

    return current
