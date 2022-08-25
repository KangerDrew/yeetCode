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


