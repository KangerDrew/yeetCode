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


print(coin_change([1, 2, 5], 11))
print(coin_change([2], 3))
print(coin_change([2, 5], 12))

