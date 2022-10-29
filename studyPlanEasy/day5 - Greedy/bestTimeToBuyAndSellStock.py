# First attempt:

def maxProfit(prices):

    current_min = float('inf')
    best_profit = 0

    for p in prices:
        current_min = min(current_min, p)
        best_profit = max(best_profit, p - current_min)

    return best_profit


# Slight improvement:

def maxProfitBetter(prices):

    current_min = float('inf')
    best_profit = 0

    for p in prices:

        if p < current_min:
            current_min = p
        else:
            best_profit = max(best_profit, p - current_min)

    return best_profit
