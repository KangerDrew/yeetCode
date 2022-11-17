# When we calculate the total sum, we need to ensure that we can  create a
# sub-array that can reach half the total sum. This means that the remaining
# value(s) will form another sub-array who's sum will be half the total sum!

# If total sum is odd value, and our values only consist of integers, we can't
# get sub-array who's sum is half the total sum!


def partitionEqualSum(nums):
    total = sum(nums)

    # If the total is non-even, it is impossible to create two sub-arrays
    # of same values...
    if total % 2 != 0:
        return False

    target = total // 2
    # Initialize a set that'll keep track of all possible sum values:
    all_sums = set()

    for n in nums:

        new_all_sums = set()
        new_all_sums.add(n)

        for s in all_sums:
            if s == target:
                return True
            elif s + n == target:
                return True
            elif s + n > target:
                new_all_sums.add(s)
                continue

            new_all_sums.add(s + n)
            new_all_sums.add(s)

        all_sums = new_all_sums

    return True if target in all_sums else False


print(partitionEqualSum([1, 5, 11, 5]))
