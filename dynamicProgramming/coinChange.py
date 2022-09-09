def coin_change_trash(coins, amount):
    if amount == 0:
        return 0

    possible_route = [None] * (amount + 1)
    possible_route[0] = []

    for i, route in enumerate(possible_route):
        if route is not None:
            for coin in coins:
                combo = route + [coin]

                if (i + coin) <= amount:
                    if possible_route[i + coin] is None or (len(possible_route[i + coin]) > len(combo)):
                        possible_route[i + coin] = combo

    return possible_route[-1]


def coin_change(coins, amount):
    if amount == 0:
        return 0

    table = [None] * (amount + 1)
    table[0] = 0

    for i, route in enumerate(table):
        if table[i] is not None:
            for coin in coins:
                test_val = table[i] + 1

                if (i + coin) <= amount:
                    if table[i + coin] is None or (table[i + coin] > test_val):
                        table[i + coin] = test_val

    return table[-1] if table[-1] is not None else -1


# print(coin_change([1, 2, 5], 11))
# print(coin_change([2], 3))
# print(coin_change([2, 5], 12))


# Attempting to solve this problem using recursive helper with memoization:
def coin_change_recur(coins, amount):

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


print(coin_change_recur([1, 2, 5], 11))
