# binary search practice:

# 13
# [10, 18, 101]
def bs(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] < target:
            left = mid + 1
        else:
            right = mid

    return left

# Attempting to write a binary search algo that returns:
def bsMin(arr, target):
    # Everything same as previous BS algo
    # up till the if else statement...
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid



arr1 = sorted([0, 1, 0, 3, 2, 3])
# [0, 0, 1, 2, 3, 3]
# print(arr1[bs(arr1, -1)])
arr2 = sorted([18, 55, 66, 2, 3, 54])
# [2, 3, 18, 54, 55, 66]
# for val in range(19, 54):
#     print(arr2[bs(arr2, val)])
arr3 = sorted([3, 5, 6, 2, 5, 4, 19, 5, 6, 7, 12])
# [2, 3, 4, 5, 5, 5, 6, 6, 7, 12, 19]
# print(arr3[bs(arr3, 11)])
arr4 = sorted([4, 10, 4, 3, 8, 9])
# [3, 4, 4, 8, 9, 10]
# for val in range(0, 10):
#     print(arr4[bs(arr4, val)])
arr5 = sorted([10, 9, 2, 5, 3, 7, 101, 18])
# [2, 3, 5, 7, 9, 10, 18, 101]
for val in range(0, 10):
    print(arr5[bs(arr5, val)])
