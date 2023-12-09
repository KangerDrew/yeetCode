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

    return pre


# Recursive solution from memory:
def reverseRecur(head):

    if not head or not head.next:
        return head

    def recur(node):
        # Edge case - We found the end of the original list:
        if not node.next:
            return node

        # First, traverse deeper into recursion:
        new_head = recur(node.next)

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


# Alternate online approach for recursive solution:
def reverseRecurAlt(head):
    # Edge case: If you are given an empty linked list, return none
    if not head:
        return None

    # Base case: If you reached the end of the list, that will be the "new head"
    # of the linked list. Return it!
    if not head.next:
        return head

    # If we have yet to reach the end of the list, we will reverse the direction of the
    # node that goes after this current stack!
    if head.next:
        # The recursive function should give us the end (newHead) of the list:
        newHead = reverseRecurAlt(head.next)
        # Reverse the direction of the node that comes after this one:
        head.next.next = head

    # This last line will make it so that when we exit out of the recursive stack,
    # the final node will be pointing towards None, instead towards the second node
    # of the original linked list:
    head.next = None

    # Return the new head:
    return newHead
