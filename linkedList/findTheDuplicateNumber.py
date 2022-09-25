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

