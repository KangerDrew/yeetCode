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
# 1) The task with most frequency can be finished if we slot all the other tasks in
# between idle times. This also means there will be no excess idle time, and the unit
# of time would simply be equal to the length of the input task array!

# ex) [A, B, A, C, D, E, F, A],   n = 2
# ==> A       B       C       A       D       E       A       F
#     MF                      MF                              MF
# time = len(tasks)

# 2) The task with most frequency needs longer time to finish their tasks even after
# slotting all other remaining tasks in between idle times. This means that the most
# frequent task will need additional idle times to be completed.

# ex) [A, A, A, B, C, A],   n = 2
# ==> A       B       C        A       i       i       A       i       i       A
#     MF                       MF                      MF                      MF
#     <---      n + 1     --->  (cool down time required before queuing same task again)
#     <===                    (n + 1) * (most_f - 1)                      ===>  <=== n_most_f ===>

# most_f = max(frequencies)  # frequencies is the array of length 26, where an index
#                            # represents the "task" (letter) and its value represents
#                            # how many times that letter is shown in the tasks array.
#                            # So, most_f will return how many times A was present!

# n_most_f = frequencies.count(most_f)  # Checks to see if there are any other tasks that
#                                       # Also has the same frequency value as most_f. In
#                                       # this example, A is predominantly most frequent
#                                       # task, so this value will be 1.


# time = (n + 1) * (most_f - 1) + n_most_f

# The expression, (n + 1) * (most_f - 1) + 1 will determine the total time required
# to only complete the most frequent task. n_most_f will be 1 for a case where one
# task is dominantly the most frequent task. For the case where A is not the only
# dominant frequency, n_most_f will return greater than 1.

# So why do we need to consider scenario 1? Though (n + 1) * (most_f - 1) + n_most_f
# seems like a foolproof solution, sometimes it will yield values below the length
# of the task. This means that the expression failed to account for leftover tasks.
# However, assuming most_f indeed gave us the number of occurrence of most frequent
# task, we can assume that in that case, just taking the length of the task array will
# return us the shortest possible time it takes to complete all tasks, without any idle
# time required!


def taskScheduleMath(tasks, n):
    frequencies = [0] * 26

    for t in tasks:
        frequencies[ord(t) - ord('A')] += 1

    # Determine the the most frequent task's frequency:
    f_max = max(frequencies)
    # Calculate how many tasks also has that exact same frequency:
    n_max = frequencies.count(f_max)

    # As mentioned in explanation earlier, compare length of the task array,
    # against the minimum time required to complete most frequent task, and
    # any that has similar frequencies:
    return max(len(tasks), (f_max - 1) * (n + 1) + n_max)
