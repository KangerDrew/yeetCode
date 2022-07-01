
# THIS IS WRONG
def insertIntervalsFALSE(intervals, newInterval):

    result = []

    for i in range(len(intervals)):

        # First if statement covers a case where the last
        # value of newInterval is less than current interval's
        # first value.
        # This means we need to insert newInterval BEFORE the
        # current interval:
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        # Next case is where the current interval's end value is
        # greater than the first value of newInterval.
        # This means we need to create a new interval by combining
        # the current interval with newInterval, and insert it into
        # the current result and return with the rest!
        elif newInterval[0] < intervals[i][1]:
            newCombinedInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]
            result.append(newCombinedInterval)
            return result + intervals[i + 1]
        # Append the current interval onto result otherwise:
        else:
            result.append(intervals[i])

    # If we completed the for loop without returning early,
    # it means the newInterval belongs to the very end of the
    # intervals:
    result.append(newInterval)
    return result



def insertIntervalsCORRECT(intervals, newInterval):

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
