# This is a cycle detection problem.
# See Course Schedule II for Topological Sort Problem!

def canFinish(numCourses, prerequisites):
    # Create adjacency list using numCourses value
    # and prerequisites list:
    prereqMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        prereqMap[crs].append(pre)

    # Now, create a set that we'll use to detect if we've already visited
    # that course (i.e. is there a cycle?)
    cycleCheck = set()

    def dfs(course):
        # Base case #1: Loop Detected
        if course in cycleCheck:
            return False
        # Base case #2: Successfully traversed to the last node with no loop
        if not prereqMap[course]:  # i.e. if prereqMap[course] is empty list
            return True

        # If neither is true, add the current course to the cycleCheck:
        cycleCheck.add(course)

        # Now, recursively run dfs on all that course's prereqs:
        for prereq in prereqMap[course]:
            # If dfs came back false, return back false to top:
            if not dfs(prereq):
                return False

        # If dfs completed without returning false,
        # remove course from cycleCheck (clean up).
        cycleCheck.remove(course)
        # We also know that if dfs returned true for all prereqs,
        # it means that next time if dfs is run on the same course,
        # we'll use the base case #2 to exit out earlier. Setting
        # prereqMap[course] to empty list will do that:
        prereqMap[course] = []
        return True

    # Loop through each course, and run dfs to see if
    # any cycles were detected (dfs will return False if
    # there is a cycle)
    for c in range(numCourses):
        if not dfs(c):
            return False

    # Otherwise, return True:
    return True


print(canFinish(5, [[0, 1], [0, 2], [1, 3], [1, 4], [3, 4]]))
