import collections


def courseScheduleII(numCourses, prerequisites):

    prereq = {c: [] for c in range(numCourses)}
    for course in prerequisites:
        prereq[course[0]].append(course[1])

    schedule = []
    visit, cycle = set(), set()

    def dfs(crs):
        if crs in cycle:
            return False

        if crs in visit:
            return True

        cycle.add(crs)
        for pre in prereq[crs]:
            if not dfs(pre):
                return False

        cycle.remove(crs)
        visit.add(crs)
        schedule.append(crs)
        return True

    for i in range(numCourses):
        if not dfs(i):
            return []

    return schedule

