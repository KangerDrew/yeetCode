# Seemingly simple yet tricky problem...


def rotateList(head, k):

    if not head:
        return head

    # Determine the length of the list:
    list_len = 1
    tail = head

    while tail.next:
        tail = tail.next
        list_len += 1

    # Adjust k value so we get less than length of the list:
    k = k % list_len
    if k == 0:
        # No need to rotate list, return the head:
        return head

    # Otherwise, we go to the position right before the new head:
    new_tail = head
    for i in range(list_len - k - 1):
        new_tail = new_tail.next

    # Get the reference to new head:
    new_head = new_tail.next
    # The new tail should refer to null:
    new_tail.next = None
    # The old tail should point back towards the beginning:
    tail.next = head

    # Return new_head:
    return new_head


