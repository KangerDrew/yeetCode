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

