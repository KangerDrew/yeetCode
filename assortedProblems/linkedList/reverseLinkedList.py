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
    if not head:
        return head


    def recursive(node):
        if not node.next:
            return node

        rev = recursive(node.next)

        # Set the .next of the node after back to the input,
        # creating a mini loop:
        node.next.next = node
        # Set the next pointer of the input to be None.
        node.next = None
        return rev

    return recursive(head)
