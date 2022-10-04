# Simplest solution is to just append every value of the list to an array, and
# increment from left and right towards the center to check if every value match:

# However, this solution costs O(n) memory. This isn't the most ideal solution...
def palindromeLLEasy(head):

    travelled = []

    while head:
        travelled.append(head.val)
        head = head.next

    left, right = 0, len(travelled) - 1

    while left < right:
        if travelled[left] != travelled[right]:
            return False

        left += 1
        right -= 1

    return True


# Instead of storing everything to an array, we could instead use two pointers.
# One pointer will go one by one, while other will go 2x that speed. This will
# make it so that once the faster pointer reach the end, the slower pointer will
# be positioned at the middle of the linked list. From there, we reverse the
# latter half portion of the linked list using the slower pointer and once finished,
# compare the first-half with the reversed-latter-half. This would be possible since
# we should still have reference to head, and slow pointer should have ended up at
# the end of the original list (now a beginning of a reversed half-list):

# Example 1:
# Input [1, 2, 2, 1] will result in following left & right linked lists:
# L: [1, 2, 2, None] R: [1, 2, None]

# Original:
# 1  =>  2  =>  2  =>  1  =>  None
# New:
# 1  =>  2  =>
#                2  => None
#        1  =>


# Example 2:
# Input [1, 2, 3, 2, 1] will result in following left & right linked lists:
# L: [1, 2, 3, None] R: [1, 2, 3, None]

# Original:
# 1  =>  2  =>  3  =>  2  =>  1  =>  None
# New:
# 1  =>  2  =>
#                3  => None
# 1  =>  2  =>

def palindromeLLBetter(head):

    slower, faster = head, head

    while faster and faster.next:
        slower = slower.next
        faster = faster.next.next

    # As shown in examples, if the linked list length is odd, slower pointer
    # will end up right at the midpoint. For even linked list, it'll end up
    # on the right side of the midsection.

    # Start reversing from where the slower pointer is. We do this by using
    # 3 pointer system:

    # First, define prev pointer as None. This None pointer is also the end
    # of the new reversed linked list:
    prev = None

    while slower:
        after = slower.next
        slower.next = prev
        prev = slower
        slower = after

    # The latter half portion is now reversed, and prev pointer is its "head"
    left, right = head, prev

    # Check that the values match:
    while right:
        if left.val != right.val:
            return False

        # Increment until the right pointer reaches end:
        left = left.next
        right = right.next

    # The values are matching backwards and forwards. Return True:
    return True
