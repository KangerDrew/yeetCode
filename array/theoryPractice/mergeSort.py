def mergeSort(arr):
    if len(arr) == 1:
        return arr

    midpoint = len(arr) // 2


def helper(l1, l2):

    combineSorted = []

    while l1 and l2:
        if l1[0] < l2[0]:
            combineSorted.append(l1.popleft())
        else:
            combineSorted.append(l2.popleft())

    if l1:
        combineSorted + l1

    if l2:
        combineSorted + l2

    return combineSorted