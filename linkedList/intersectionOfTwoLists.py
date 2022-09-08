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
# <    A    > <       C       >
# B1 => C1 => C2 => C3 => NONE
# < B > <       C       >
# Let's label comp

# Now, try adding two separate lists, twice in different order:
# A1 => A2 => C1 => C2 => C3 => B1 => C1 => C2 => C3 => NONE
# B1 => C1 => C2 => C3 => A1 => A2 => C1 => C2 => C3 => NONE
# <    A    > < B > <       C       >

# The length of each lists is: A + B + 2C
# Note that the intersection occurs C distance from the end of the list.

