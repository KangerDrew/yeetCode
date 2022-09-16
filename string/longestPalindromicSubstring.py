# We COULD use dynamic programming approach to solve this problem... but there is a
# easier way...

# We can loop through the string once, and at a select index, expand outwards using
# two pointers to check that a palindrome can be constructed, using that index as a
# center.

# If the two index starts at the same center point, we will get the longest ODD number
# length palindrome. If two index starts 1 index apart from each other, we will get the
# longest EVEN number length palindrome!


