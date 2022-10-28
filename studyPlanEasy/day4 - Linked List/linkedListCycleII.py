# This problem uses Floyd-Warshall algorithm to determine the cycle location.
# Idea is this - use two pointers (slow pointer that increments once per loop, fast
# pointer that increments twice per loop) to detect cycle. If the cycle is detected,
# we move one of the pointers back to the beginning, and begin incrementing both
# pointers by 1. The two pointers will collide again, at the point where the cycle begins!

def listCycleII(head):
    # If the list is too short or there's no cycle, return null node:
    if not head or not head.next:
        return None

    # Initialize two pointers as stated above:
    p1, p2 = head.next, head.next.next


