def insertIntervals(intervals, newInterval):

    result = []

    # Side note 1: I tried switching the order of the two initial if and elif
    # statements, and both resulted in correct answer!
    for i in range(len(intervals)):
        # Check if last value of the newInterval is less than the first value of current
        # intervals[i]. If so, it means we can append the newInterval to the result, then,
        # append the remaining intervals to the result (exit out of for loop and the function
        # by returning the result here!):
        if newInterval[1] < intervals[i][0]:
            result.append(newInterval)
            return result + intervals[i:]
        # Check if the initial value of the newInterval is greater than the last value of the
        # current intervals[i]. If true, we append the current intervals[i] to the result. We
        # don't know if the next interval will overlap with newInterval, so we proceed with the
        # for loop:
        elif newInterval[0] > intervals[i][1]:
            result.append(intervals[i])
        # If neither statement are true, that means we need to update the current newInterval
        # by merging it with the current intervals[i]. Proceed with the for loop:
        else:
            newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

    # If we completed the for loop without returning early,
    # it means the newInterval belongs to the very end of the
    # intervals:
    result.append(newInterval)
    return result
