# My first approach was to use hash set, where we'd store all the
# nodes of one of the list and then iterate through the second list
#  and check to see if the node already exists in the hash set:


def intersectionHashSet(headA, headB):

    stored = set()

    while headA:

        stored.add(headA)
        headA = headA.next

    while headB:

        if headB in stored:
            return headB

        headB = headB.next

    return None


# There is a way to solve this problem without using hash set (O(1) memory)
# It involves the use of two pointers...

# Example:
# A1 => A2 =>
#             C1 => C2 => C3 => NONE
#       B1 =>

# We can visualize the above intersecting linked list as two separate lists:
# A1 => A2 => C1 => C2 => C3 => NONE
# <    A    > <          C          >
# B1 => C1 => C2 => C3 => NONE
# < B > <          C          >
# Let's label comp

# Now, try adding two separate lists, twice in different order:
# A1 => A2 => C1 => C2 => C3 => NONE => B1 => C1 => C2 => C3 => NONE
# B1 => C1 => C2 => C3 => NONE => A1 => A2 => C1 => C2 => C3 => NONE
# <    A    > < B > <          C          >

# The length of each lists is: A + B + 2C
# Note that the intersection occurs C distance from the end of the list.
# If we iterate A + B + C distance from the root of either list, we will
# always end up at the intersection point (assuming there is one). Sometimes
# the intersection can be reached earlier, but only if distance A and B are
# equal.


def intersectionPointers(headA, headB):

    # Initialize 2 pointers:
    p1, p2 = headA, headB

    # This while loop will persist until one of the following scenarios:
    # Scenario 1A - Intersection is reached after length A + B + C
    # Scenario 1B - Intersection is reached after length A or B (A and B have same length)
    # Scenario 2 - No intersection exists, and while loop exists after both pointers reach
    # the None at the end of the length of two combined list (end of A + B + 2C)

    while p1 != p2:

        p1 = p1.next if p1 else headB
        p2 = p2.next if p2 else headA

    # The while loop above will always exit, either when we find the intersection,
    # or when we reach the end of the two combined list. Once that happens, we return
    # either one of the pointer:
    return p1

