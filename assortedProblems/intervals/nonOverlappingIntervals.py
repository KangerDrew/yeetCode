def nonOverlappingIntervals(intervals):

    count = 0
    intervals.sort(key=lambda elem: elem[0])
    currentMin = float('-inf')

    filtered = []
    for interval in intervals:

        if interval[0] == currentMin:
            count += 1
            pass
        else:
            currentMin = interval[0]
            filtered.append(interval)

    for interval in filtered:
        # GAVE UP HERE
        pass

    return count


# The approach for non-overlapping interval is to sort the provided
# interval list by their first interval value, and keep track of a count
# value...

def nonOverlappingIntervalsAttempt(intervals):

    # Sort:
    intervals.sort(key=lambda i: i[0])

    # count will keep track of how many "intervals" would have to be removed:
    count = 0
    # recentEnd will keep track of the "previous interval's end value", which
    # we need in order to determine which interval is to be removed:
    recentEnd = intervals[0][1]

    # Iterate from the 2nd element of the intervals list:
    for j in range(1, len(intervals)):

        # Check whether the beginning of the interval conflicts with the previous end:
        if intervals[j][0] < recentEnd:
            # If there was a conflict, that means an interval needs to be removed:
            count += 1
            # We need to "remove" the interval with the greater end value. We can simulate
            # this by updating our recentEnd value by taking the smaller one:
            recentEnd = min(recentEnd, intervals[j][1])
        else:
            # If there were no conflicts, then we don't remove any interval and simply update
            # the recentEnd value with our current interval's end value:
            recentEnd = intervals[j][1]

    return count

