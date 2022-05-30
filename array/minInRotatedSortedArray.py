def findMin(nums):
    res = nums[0]
    left, right = 0, len(nums) - 1

    while left <= right:
        leftVal = nums[left]
        rightVal = nums[right]
        if leftVal < rightVal:
            res = min(res, leftVal)
            break

        middle = (left + right) // 2
        midVal = nums[middle]
        res = min(res, midVal)

        if midVal >= leftVal:
            left = middle + 1
        else:
            right = middle - 1

    return res


print(findMin([4, 5, 6, 7, 2, 3]))
print(findMin([2, 1]))
print(findMin([6, 1, 2, 3, 4, 5]))
print(findMin([2, 3, 4, 5, 1]))
