import heapq

# We need to do more than just sort the interval by their first value...

# Alternate method 1 - Use Priority Queue (min heaps!)
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
    # Initialize a heap (ongoing meetings), but first add the first meeting:
    ongoing_meetings = [intervals[0]]
    heapq.heapify(ongoing_meetings)


    return len(ongoing_meetings)


def meetingRoomsII(intervals):
    intervals.sort(key=lambda i: i[0])
