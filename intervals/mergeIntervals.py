

def mergeIntervals(intervals):
    # Sort the fking intervals:
    intervals.sort(key=lambda i: i[0])

    # Add the first interval from the sorted interval:
    final_intervals = [intervals[0]]

    for interval in intervals[1:]:

        # Grab the "max" from the most recent entry of final_intervals:
        recentMax = final_intervals[-1][1]

        # If the first value of the interval is less than recentMax,
        # we will be modifying the most recent interval by changing
        # the max value.
        # IMPORTANT: We do NOT have to worry about modifying the min
        # value (leftmost value), since the intervals array is now sorted
        # by the min value and we know for sure that min values of
        # the following intervals in the array will NOT be greater...
        if interval[0] <= recentMax:
            # Take the greatest between recentMax, and interval[1]
            final_intervals[-1][1] = max(recentMax, interval[1])

        # if above is not true, simply append the interval as we do not
        # need to modify the most recent interval in final_intervals
        else:
            final_intervals.append(interval)

    return final_intervals

