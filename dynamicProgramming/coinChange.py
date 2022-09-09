# Bottom up approach, where we use array to keep track of minimum
# number of coin to reach a certain index (amount):
def coin_change(coins, amount):
    if amount == 0:
        return 0

    # Initialize an array of length amount + 1. Index 0 represents
    # number of coins to reach amount 0, index 1 represents number
    # of coins to reach 1, etc...

    # Set default value to float('inf') for all index, except 0, where
    # it takes 0 coins to reach amount 0:
    memo = [float('inf') for i in range(amount + 1)]
    memo[0] = 0

    for i in range(amount + 1):

        if memo[i] != float('inf'):
            for c in coins:
                possible_min = memo[i] + 1
                if i + c < amount + 1:
                    memo[i + c] = min(memo[i + c], possible_min)

    return memo[-1] if memo[-1] != float('inf') else -1


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([2, 5], 12))


# Attempting to solve this problem using recursive helper with memoization:
def coin_change_topdown(coins, amount):

    # Edge case: If 0 is entered, return 0
    if amount == 0:
        return 0

    # Initialize a memoization hash map, which will keep
    # track of the ideal minimum number of coins to reach
    # a certain amount:
    memo = {}
    def helper(remainder):
        # If the result was already found previously, return it from
        # the memoization dictionary:
        if remainder in memo:
            return memo[remainder]
        # Edge case #1 - We've reached the root. Return 0:
        if remainder == 0:
            return 0
        # Edge case #2 - Entered input amount cannot be reached, return
        # very large value for comparison:
        if remainder < 0:
            return float('inf')

        # Initialize a value we'll use to keep track of lowest
        # possible # of coins. This should be very large:
        min_val = float('inf')

        # Loop through each coin in coins array, and see what minimum value they
        # return. Compare and see which "path" returned the lowest amount of coins,
        # and use that as a min_val:
        for c in coins:
            min_val = min(helper(remainder - c) + 1, min_val)

        # Store the returned min_val, and return it:
        memo[remainder] = min_val
        return min_val

    # Run the helper function:
    helper(amount)
    # Check the memoization hash map and return the result for the "amount" input.
    # If the value is float('inf') that means we couldn't find a possible solution
    # so return -1 instead:
    return memo[amount] if memo[amount] != float('inf') else -1


# print(coin_change_topdown([1, 2, 5], 11))
