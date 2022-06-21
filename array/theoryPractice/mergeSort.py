def mergeSort(arr):
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2

    left, right = mergeSort(arr[:midpoint]), mergeSort(arr[midpoint:])

    return helper(left, right)


def helper(l1, l2):

    combineSorted = []

    while l1 and l2:
        if l1[0] < l2[0]:
            popped = l1.pop(0)
            print(popped)
            combineSorted.append(popped)
        else:
            popped = l2.pop(0)
            print(popped)
            combineSorted.append(popped)

    if l1:
        # combineSorted + l1
        combineSorted.extend(l1)
    if l2:
        combineSorted.extend(l2)
        # combineSorted + l2

    return combineSorted


def mergeSortCopied(arr):
    if len(arr) <= 1:
        return arr

    midpoint = len(arr) // 2

    left, right = mergeSortCopied(arr[:midpoint]), mergeSortCopied(arr[midpoint:])

    return merge(left, right)


def merge(left, right):

    result = []
    leftPointer = rightPointer = 0

    while leftPointer < len(left) and rightPointer < len(right):

        if left[leftPointer] < right[rightPointer]:
            result.append(left[leftPointer])
            leftPointer += 1
        else:
            result.append(right[rightPointer])
            rightPointer += 1

    result.extend(left[leftPointer:])
    result.extend(right[rightPointer:])

    return result


print(mergeSort([3, 2, 5, 1, 4]))
print(mergeSortCopied([3, 2, 5, 1, 4]))
