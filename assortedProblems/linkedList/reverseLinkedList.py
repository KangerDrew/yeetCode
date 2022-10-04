# My first blind attempt at reverse linked list:

# WRONG
def reverse(head):
    # Edge case - List only consists of one node:
    if not head.next:
        return head

    pre = None
    current = head
    after = head.next

    while current:

        current.next = pre
        pre = current
        current = after
        after = after.next

        if not after:
            return current


def reverseCORRECTED(head):
    # Edge case #1 - List is empty
    if not head:
        return None

    # Edge case #2 - List only consists of one node:
    if not head.next:
        return head

    # Set up 3 pointers to help us traverse down the list:
    pre = None
    current = head
    after = head.next

    # Use while loop to traverse down the list:
    while current:

        # Point current node backwards towards pre:
        current.next = pre
        # Move pre pointer to current:
        pre = current

        # Check if our after pointer is null. If so, it means we've
        # finished reversing and must return the current node:
        if not after:
            return current

        # Move current pointer to after:
        current = after
        # Move after pointer to the node after that:
        after = after.next


# Shorter cleaner solution than the previous one:
def reverseShorter(head):
    prev = None

    while head:
        after = head.next
        head.next = prev
        prev = head
        head = after

    return prev


# Recursive solution:
def reverseRecursive(head):
    # Edge case in case empty linked list is entered:
    if not head:
        return head

    # The purpose of the recursive function is to traverse deep into
    # the linked list until the end is reached. From there, as each
    # recursion stack is removed, we'll be reversing the direction of
    # each node and return the "end" of the list back to the top:
    def recursive(node):
        # Return condition here indicates we've reached the end of the
        # list, and we can return the end:
        if not node.next:
            return node

        # If the above statement didn't trigger, we need to traverse
        # deeper into the linked list to get the end of the list (which
        # will be the head of the reversed list)
        last_node = recursive(node.next)

        # With the exception of the case where we're at the very end,
        # we are in the middle of a linked list. We need to reverse
        # the direction of the node that comes after. Set the next
        # value of the next node to be
        node.next.next = node

        # Optionally, we can set the .next value to be Null node at each
        # stack. But this will not be necessary since at each stack level
        # after removing this one, we'll be resetting the direction. The
        # only reason why we'd set the next node to null is so that after
        # we've reached the very end (back to the original head node), the
        # original head node will be pointing towards the None, since it's
        # now the end of the reversed list:
        # node.next = None

        # Return the recursively obtained last_node:
        return last_node

    # Use recursive helper function to reverse the list, and get the last
    # node of the list.
    end_node = recursive(head)
    # Now, we still have the reference to the original head. But if we didn't
    # set "node.next = None" on each recursion stack, we'll currently have a
    # reversed linked list where the last node is pointing back to the second
    # last node (mini-cycle at the end). So fix this by setting head.next to
    # None instead!
    head.next = None

    # Return the end_node, which is now the new head of the reversed linked list!
    return end_node
