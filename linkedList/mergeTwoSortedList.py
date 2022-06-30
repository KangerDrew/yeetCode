class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoList(list1, list2):

    # Initialize a dummy node to append our node to:
    pre_head = ListNode()
    # We need a pointer that we can use to
    # append new node:
    current = pre_head

    # Use while loop to check list1 and list2 while they're not null:
    while list1 and list2:

        # Check which node has a smaller value, and append the smaller one:
        if list1.val > list2.val:
            current.next = list2
            list2 = list2.next
        else:
            current.next = list1
            list1 = list1.next

        # Increment the pointer:
        current = current.next

    # Check if there were any un-appended node from either list1 or list2:

    if list1:
        current.next = list1

    if list2:
        current.next = list2

    # return the node after the pre_head dummy node:
    return pre_head.next
