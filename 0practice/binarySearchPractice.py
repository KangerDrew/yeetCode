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
            # it seems that not truncating the right pointer
            # makes the binary search function always return
            # a value that's larger than intended target, if
            # target is not in the array!!!
            right = mid

    return left


# Attempting to write a binary search algo that returns smaller value
# if target doesn't exist in the arr:

# [2, 3, 5], 4
def bsMin(arr, target):
    # Everything same as previous BS algo
    # up till the if else statement...
    left = 0
    right = len(arr) - 1

    while left < right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid

        if arr[mid] > target:
            right = mid - 1
        else:
            # Unlike previous version, we
            left = mid + 1

    # This if statement will decrement the pointer, depending
    # on whether the result is greater than the intended target
    # or not. Also make sure we don't go out of bounds:
    if target < arr[left] and left > 0:
        left -= 1

    return left


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
arr5 = sorted([10, 9, 2, 5, 3, 7, 101, 18, 10, 10, 10])
# [2, 3, 5, 7, 9, 10, 18, 101, 10, 10, 10]
for val in range(11, 30):
    print("testing " + str(val))
    print(arr5[bsMin(arr5, val)])
