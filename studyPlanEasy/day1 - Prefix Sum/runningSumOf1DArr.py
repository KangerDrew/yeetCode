# My first blind attempt:

def runningSum(nums):

    arr = []
    current = 0

    for n in nums:
        current += n
        arr.append(current)

    return arr


def runningSumAlt(nums):

    arr = [nums[0]]
    for i, n in enumerate(nums[1:]):
        arr.append(arr[i] + n)

    return arr


def runningSumChangeInput(nums):

    for i in range(1, len(nums)):
        nums[i] = nums[i - 1] + nums[i]

    return nums
