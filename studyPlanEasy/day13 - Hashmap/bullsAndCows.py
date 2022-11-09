# paper and pencil game, where you guess the "secret" value and return how many
# integers were guessed correctly AND in the same position (Bulls) and how many
# were in the secret value but are not in correct position (Cows)

def twoPassBullsAndCows(secret, guess):
    # Dictionary for Lookup
    lookup = {}
    for s in secret:
        lookup[s] = lookup.get(s, 0) + 1

    x, y = 0, 0

    # First finding numbers which are at correct position and updating x
    for i in range(len(guess)):
        if secret[i] == guess[i]:
            x += 1
            lookup[secret[i]] -= 1

    # Finding numbers which are present in secret but not at correct position
    for i in range(len(guess)):
        if guess[i] in lookup and secret[i] != guess[i] and lookup[guess[i]] > 0:
            y += 1
            lookup[guess[i]] -= 1

    # The reason for using two for loop is in this problem we have
    # to give first priority to number which are at correct position,
    # Therefore we are first updating x value

    return "{}A{}B".format(x, y)
