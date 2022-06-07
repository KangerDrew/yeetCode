# This solution is very similar to the other course schedule variant question, but the dfs behaves
# slightly differently since what we're returning is a list of all the nodes, instead of a boolean:

def findOrder(numCourses, prerequisites):
    # Create adjacency list using numCourses value
    # and prerequisites list:
    prereqMap = {i: [] for i in range(numCourses)}
    for crs, pre in prerequisites:
        prereqMap[crs].append(pre)

    # We need to create two sets, one for dfs traversal (visitedSet)
    # and another to check if there's a cycle (cycleCheck - Same as
    # previous problem!)
    visitedSet, cycleCheck = set(), set()

    # We need a list that'll keep track of the sorted order of courses
    output = []

    def dfs(course):
        # Base case #1: Loop Detected
        if course in cycleCheck:
            return False
        # Base case #2: We've already visited the current node (course)
        if course in visitedSet:
            return True

        # If neither is true, add the current course to the cycleCheck:
        cycleCheck.add(course)

        # Recursively run dfs on all that course's prereqs:
        for prereq in prereqMap[course]:
            if not dfs(prereq):
                return False

        # Once recursion is complete, cleanup the cycleCheck
        # by removing the course from it:
        cycleCheck.remove(course)
        # Add the course to the visited set, so we won't need
        # to traverse it again:
        visitedSet.add(course)
        # Append the course to the output list:
        output.append(course)

        return True

    # Loop through each course, and run dfs to build
    # the topologically sorted list of nodes (courses):
    for c in range(numCourses):
        if not dfs(c):
            return []

    # Returned the output list:
    return output


print(findOrder(2, [[1, 0]]))
