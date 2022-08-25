# My first attempt at detecting linked list cycle problem:

def hasCycle(head):
    # Edge case - Nothing in Linked List, means no cycle
    if not head:
        return False

    pointer1 = head
    pointer2 = head

    while pointer2:

        pointer1 = pointer1.next
        pointer2 = pointer2.next

        if not pointer2:
            return False

        pointer2 = pointer2.next

        if pointer1 == pointer2:
            return True

    return False


# Cleaner, shorter solution:
def hasCycleClean(head):
    slow, fast = head, head

    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

        if slow == fast:
            return True

    return False
