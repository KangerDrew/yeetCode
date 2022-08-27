# This problem asks if there are any overlaps in the provided intervals.
# Approach is very similar to mergeIntervals problem, but we just simply
# return True/False depending on whether we find an overlap or not:

def meetingRooms(intervals):
    # Sort the array, based on the first value of the interval:
    intervals.sort(key=lambda x: x[0])

    # Loop through the intervals list, starting from index 1:
    for i in range(1, len(intervals)):

        # Check if the ending value of the previous interval is greater than
        # the starting value of the current interval. If so, that means there
        # is an overlap, and we return False:
        if intervals[i - 1][1] > intervals[i][0]:
            return False

    # If the above loop didn't return False, that means there's no overlap:
    return True

