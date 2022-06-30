def removeNthFromEnd(head, n):

    current1 = head
    current2 = head

    list_length = 0

    while current1:
        current1 = current1.next
        list_length += 1

    if list_length == n:
        return head.next

    target = list_length - n - 1

    while target > 0:
        target -= 1
        current2 = current2.next

    current2.next = current2.next.next

    return head

