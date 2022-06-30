def removeNthFromEnd(head, n):

    # Use two pointers:
    # First pointer will be used to determine the length of the provided linked list
    # Second pointer will be used to reach the node prior to the removal node
    current1 = head
    current2 = head

    # Variable to keep track of length of list:
    list_length = 0

    # Use while loop to increment first pointer and count the length of linked list:
    while current1:
        current1 = current1.next
        list_length += 1

    # Edge case - if n is equal to the length of the node, it means first node needs to
    # be removed. Simply return "head.next" to do this.

    # The reason why we do this is because the function written afterwards can't handle
    # a case where we need to remove the first node...
    if list_length == n:
        return head.next

    # Calculate the distance we need to travel to reach the node PRIOR to the one we're
    # removing - length of list - n - 1:
    target = list_length - n - 1

    # Use while loop to reach the target. As seen here by the while loop condition, if
    # the list length is same as n, it'll result in -1 target value, which will yield
    # incorrect result. Thus, we have the if statement before target calculation to account
    # for this edge case!
    while target > 0:
        target -= 1
        current2 = current2.next

    # The current pointer should be at the node before the node we need to remove.
    # Change the .next reference to the node AFTER the removal node:
    current2.next = current2.next.next

    # Return the head:
    return head

