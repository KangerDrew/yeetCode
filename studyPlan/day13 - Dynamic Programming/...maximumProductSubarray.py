def maxProductSubarr(nums):
    # Set the maximum to lowest possible value initially:
    finalMax = float('-inf')
    # Define two variables that'll keep track of largest
    # positive AND negative values:
    curMax, curMin = 1, 1

    for n in nums:
        temp = n * curMax

        # Determine the newest curMax and curMin.
        # Largest number may occur from following scenarios:
        # 1) The product of current value and the curMax
        # 2) The product of current value and the curMin
        # 3) The current value itself (meaning we need to see if starting
        # the sub-array fresh from this point in iteration will result in
        # larger curMax or smaller curMin)
        curMax = max(temp, n * curMin, n)
        curMin = min(temp, n * curMin, n)

        print("curMax is {} and curMin is {}".format(curMax, curMin))

        # Update the final_max value if curMax has exceeded it:
        finalMax = max(curMax, finalMax)

    return finalMax


print(maxProductSubarr([2, 3, -2, 2, 10]))
