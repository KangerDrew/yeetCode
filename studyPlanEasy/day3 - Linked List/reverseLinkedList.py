# Classic problem. Solve it both iteratively and recursively:

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseItr(head):
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


# One less line:
def reverseItrImproved(head):
    if not head or head.next:
        return head

    pre = None
    current = head

    while current:
        post = current.next
        current.next = pre
        pre = current
        current = post

    return


# Recursive solution from memory:
def reverseRecur(head):

    if not head or not head.next:
        return head

    def recur(node):
        # Edge case - We found the end of the original list:
        if not node.next:
            return node

        # First, traverse deeper into recursion:
        new_head = recur(node)

        # Flip the next node's pointer:
        after = node.next
        after.next = node

        # Return the "new head" of the reversed list:
        return new_head

    # Get the new head:
    final = recur(head)

    # At this point, there's going to be a cycle at the end of the newly
    # reversed list. Flip it so it points to None. We still have access
    # to it from "head" variable:
    head.next = None
    # Return the head of the reversed list:
    return final

