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

    intervals.sort(key=lambda i: i[0])
    count = 0
    recentEnd = intervals[0][1]

    for j in range(1, len(intervals)):

        if intervals[j][0] < recentEnd:
            count += 1
            recentEnd = min(recentEnd, intervals[j][1])
        else:
            recentEnd = intervals[j][1]

    return count

