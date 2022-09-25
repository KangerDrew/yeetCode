# Initially, this problem may not seem like a linked list problem.
# You're given an array of numbers, and asked to find a duplicate.

# The important things to note here are:
# Condition 1 - length of the array is: n + 1
# Condition 2 - range of numbers in the array is: 1 <= nums[i] <= n
# Condition 3 - All integers in nums appear ONLY ONCE except for
# PRECISELY ONE INTEGER which appears two or more times.


# Approach 1: Brute Force
# Brute force approach would involve looping through the array O(n^2)
# times, comparing each value with another value in array to see if
# they're the same. Though this is solution would give us  constant
# space complexity, it's way too slow...


# Approach 2: Sort and check
# This would involve sorting the given array, and checking for duplicate
# numbers. Though better than last solution in time complexity, (O(n log n)),
# this solution would cost us more space complexity, as best sorting
# algorithms would take O( log n ) space (quick sort), or in python's case,
# it would take O(n) space complexity in worst-case scenario


# Approach 3: Use set to track
def findTheDupeNumSet(nums):
    # No return statement outside for loop required, because
    # of the constraints
    checked = set()
    for n in nums:
        if n in checked:
            return n
        checked.add(n)

# Best Approach: Treat it like a linked list problem
# If we treat the index of the array element as a node, and the value of the
# array as the pointer to "the next node", we can simulate a linked list
# behavior. looking back at all the conditions for the problem, the linked
# list that we'll get will always have a cycle (see videos & examples for
# further illustrations...

# This solution runs at O(n) time complexity, with O(1) space complexity:
def findTheDupeNumLL(nums):


# Start two pointers at index 0
    slow, fast = 0, 0

    # Increment slow pointer by 1, fast
    # pointer by 2
    while True:
        slow = nums[slow]
        fast = nums[nums[fast]]

        # If pointers intersect, break out:
        if slow == fast:
            break

    # Using floyd-warshall algorithm, if we move one of the
    # pointer back to the starting point and increment each
    # pointer one step at a time, they will always collide
    # at where the loop starts!

    fast = 0
    while slow != fast:
        slow = nums[slow]
        fast = nums[fast]

    # Return the intersection value:
    return slow