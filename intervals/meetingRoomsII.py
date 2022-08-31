import heapq


# We need to do more than just sort the interval by their first value...

# Method 1 - Use Priority Queue (min heaps!)
# Idea is to first sort the intervals by their initial value, then we
# create a min-heap (python's heapq is min-heap by default) that keeps
# track of each meeting's end time. The min value of this heap will give
# us the earliest end time of the meetings currently present in the heap.
# From there, we simply iterate through all the intervals, adding them
# onto the heap if the earliest end time is greater than the starting time
# of the interval, OR performing pushpopping if the opposite is true (i.e.
# a room will be freed-up so we can remove from the priority queue). In
# the end, we return the length of the heapq as that'll tell us how many
# rooms will be needed (this is because we ONLY remove rooms when the new
# interval we're adding does not conflict with the earliest ending time).

def meetingRoomsIIHeap(intervals):
    intervals.sort(key=lambda i: i[0])
    # Initialize a heap (ongoing meetings), but first add the end
    # time of the first meeting:
    ongoing_meetings = [intervals[0][1]]
    heapq.heapify(ongoing_meetings)

    # Now, loop through the remaining meetings (everything except
    # the first one):
    for meeting in intervals[1:]:

        # Check if the current meeting's starting time will conflict
        # with the earliest end time in the heap:
        if ongoing_meetings[0] > meeting[0]:
            # If an existing room won't be available, we need to add the
            # current meeting's end time to the heap:
            heapq.heappush(ongoing_meetings, meeting[1])
        else:
            # Otherwise, an existing room can be emptied and the current
            # meeting can take place there instead:
            heapq.heappushpop(ongoing_meetings, meeting[1])

    # Return the length of the ongoing_meetings, as it'll contain only the
    # meetings that didn't get removed unless necessary:
    return len(ongoing_meetings)


# Method 2 - Assess beginning and ending separately:
# This requires the beginning and end to be sorted separately!!

def meetingRoomsII(intervals):

    beginningTimes = [i[0] for i in intervals]
    endingTimes = [j[1] for j in intervals]

    beginningTimes.sort()
    endingTimes.sort()

    maxCount, currentCount = 0, 0

    b, e = 0, 0

    while b < len(intervals):

        if beginningTimes[b] < endingTimes[e]:
            b += 1
            currentCount += 1
        else:
            e += 1
            currentCount -= 1

        maxCount = max(maxCount, currentCount)

    return maxCount

