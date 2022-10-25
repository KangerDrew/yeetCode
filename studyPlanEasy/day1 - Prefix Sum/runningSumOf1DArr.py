# My first blind attempt:

def runningSum(nums):

    arr = []
    current = 0

    for n in nums:
        current += n
        arr.append(current)

    return arr

