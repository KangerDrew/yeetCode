# One possible solution involves the use of max heap, to keep track of which
# "task" (letter) has the highest count, and prioritizing the elimination of
# those letters first, and maximize the amount we alter the tasks to reduce
# the total amount of time spent.


def taskSchedule(tasks, n):
    if n == 0:
        return len(tasks)


# If you can remember the solution below, it's great. Otherwise, max heap solution
# above is most logical and straight forward approach to this problem...

# This alternate approach uses "math" logic to determine the minimum time.

# There are two possible scenarios we can consider:
# 1) The task with most frequency can be finished if we slot all the

# 2) The task with most frequency needs longer time to finish their tasks even after
#
def taskScheduleMath(tasks, n):

    frequencies = [0] * 26

    for t in tasks:
        frequencies[ord(t) - ord('A')] += 1

    # Determine the the most frequent task's frequency:
    f_max = max(frequencies)
    # Calculate how many tasks also has that exact same frequency:
    n_max = frequencies.count(f_max)

    return max(len(tasks), (f_max - 1) * (n + 1) + n_max)
