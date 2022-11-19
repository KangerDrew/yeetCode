# New linked list problem, trickier than it looks...

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairsItr(head):

    # Initialize a dummy node that points to the head. This dummy node will
    # be used later to get the head of the newly arranged list. It's value
    # doesn't matter, as long as it points to the head:
    dummy = ListNode(0, head)

    # Initialize the pointers:
    pre, current = dummy, head

    while current and current.next:

        # Get the reference to the next "current" node:
        next_curr = current.next.next
        # Define the node to be swapped from current node:
        to_swap = current.next

        # Swap the nodes so that to_swap comes before current:
        to_swap.next = current
        current.next = next_curr

        # We also need to make it so that our pre node is pointing
        # at the to_swap node, so that it is correctly referencing
        # the "new head":
        pre.next = to_swap

        # Finally, set up so that the pre and next are referencing
        # correct nodes for swapping:
        pre = current
        current = next_curr

    # Once while loop exits, we return dummy.next, which should be
    # correctly referencing the first to_swap node now, instead of the
    # current (head) node.

    # However, if the while loop didn't trigger (because list is too short)
    # then we'll just get the head instead:
    return dummy.next


def swapPairsRec(head):

    def helper(node):
        # Exit condition - No nodes to swap:
        if not node or not node.next:
            return node

        current = node
        to_swap = current.next
        after = helper(to_swap.next)

        to_swap.next = current
        current.next = after

        return to_swap

    return helper(head)


