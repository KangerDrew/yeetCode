# Below approach is fine, but there's a faster way to do this...

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def removeNthFromEnd(head, n):

    # Use two pointers (we can also just use 1, but I used 2 for clarity):
    # First pointer will be used to determine the length of the provided linked list
    current1 = head

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

    # Second pointer will be used to reach the node prior to the removal node
    current2 = head

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


# Increment one of the pointers by n, then start incrementing both
# pointer until the one ahead reaches the end. THEN remove the node!

# THE SOLUTION BELOW IS WRONG! THIS WILL CAUSE PROBLEM WHEN ATTEMPTING TO
# REMOVE THE VERY LAST NODE:

# def removeNthNodeOnePassWRONG(head, n):
#
#     p1, p2 = head, head
#
#     # Increment p2 ahead:
#     while n > 0:
#         p2 = p2.next
#         n -= 1
#
#     # Increment both pointers right before p2 goes
#     # to null
#     while p2.next:
#         p1 = p1.next
#         p2 = p2.next
#
#     # "Remove" the node right after p1
#     p1.next = p1.next.next
#
#     return head


def removeNthNodeOnePass(head, n):
    # To avoid problem we had with previous problem, we need to implement a dummy node
    # before the head node. From very first solution (non-single pass), we observed how
    # we had to find the node BEFORE the one we needed to remove:
    dummy = ListNode(0, head)

    # Define two pointers:
    # behind - used to get the node right before the removing one
    # ahead - used to increment n times ahead, then increment together with "behind"
    # pointer to determine where to remove the node:
    behind = dummy
    ahead = head

    # Increment ahead pointer by n times:
    while n > 0:
        ahead = ahead.next
        n -= 1

    # Increment both pointers until ahead pointer reaches the end:
    while ahead:
        behind = behind.next
        ahead = ahead.next

    # Behind pointer is now positioned right before the one that needs removal.
    # Remove the "next" pointer:
    behind.next = behind.next.next

    # We can't just remove "head" since it might have been removed. Instead,
    # return dummy.next:
    return dummy.next
