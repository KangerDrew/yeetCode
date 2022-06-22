# Similar to the twoSums problem, we could loop through the array twice
# to determine the best possible profit. However, we can instead solve this
# after only passing through the input array once:

def maxProfit(prices):

    # We keep two variables in track - one called max_profit that will
    # keep track of the largest profit value, and another called lowest_val
    # which will be the lowest value that's encountered:
    max_profit = 0
    # Set the lowest_val to the largest possible value in python:
    lowest_val = float("inf")

    for price in prices:

        if lowest_val > price:
            # New lowest value is discovered. There's no need to calculate
            # the new possible max since this discovery means that there's
            # been a dip in prices. Thus, we only update the lowest_val:
            lowest_val = price
        else:
            # If the lowest value is still valid, we take the difference between
            # the current "price" value and the lowest_val, and compare it against
            # the recorded max_profit:
            max_profit = max(max_profit, price - lowest_val)

    return max_profit
