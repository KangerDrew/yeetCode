def insertIntervals(intervals, newInterval):

    result = []

    for i in range(len(intervals)):
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
    # If we completed the for loop without returning early,
    # it means the newInterval belongs to the very end of the
    # intervals:
    result.append(newInterval)
    return result
