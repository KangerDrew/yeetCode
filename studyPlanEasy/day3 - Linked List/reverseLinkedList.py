# Classic problem. Solve it both iteratively and recursively:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseLinkedListItr(head):
    # Edge cases
    if not head or not head.next:
        return head

    pre = None
    current = head
    post = head.next

    while post:
        # Change direction
        current.next = pre

        # Move pointers
        pre = current
        current = post
        post = post.next

    # Change direction one last time!
    current.next = pre

    return current
