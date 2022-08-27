# This problem asks if there are any overlaps in the provided intervals.
# Approach is very similar to mergeIntervals problem, but we just simply
# return True/False depending on whether we find an overlap or not:

def meetingRooms(intervals):
    # Sort the array, based on the first value of the interval:
    intervals.sort(key=lambda x: x[0])

    for i in range(1, len(intervals)):

        if intervals[i - 1][1] > intervals[i][0]:
            return False

    return True

