import collections
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


# We make a one-pass solution, where we use a single dictionary.
# As we loop through, the secret string will give positive contribution
# to the count, while guess string will give negative contribution!

# int(h[s] < 0) expression returns 1, if guess contains more s characters
# than secret

# int(h[g] > 0) expression returns 1, if secret contains more g characters
# than guess

# 1807
# 7810

def onePass(secret, guess):
    h = collections.defaultdict(int)
    bulls = cows = 0

    for i in range(len(secret)):

        s = secret[i]
        g = guess[i]

        if s == g:
            bulls += 1
        else:
            cows += int(h[s] < 0) + int(h[g] > 0)
            h[s] += 1
            h[g] -= 1

    return "{}A{}B".format(bulls, cows)


onePass('1807', '7810')


# I re-wrote the one-pass solution so it's easier to understand. Requires
# more memory however...

def onePassAlt(secret, guess):

    s_dic = collections.defaultdict(int)
    g_dic = collections.defaultdict(int)
    bulls = cows = 0

    for i in range(len(secret)):

        s = secret[i]
        g = guess[i]

        if s == g:
            bulls += 1
        else:

            # The objective here is to observe both the secret and the guess string
            # simultaneously on each loop. When s and g do not match, we check both
            # letters to see if either of them has occurred previously in the other
            # string. If we discovered that we've already seen the particular letter
            # in the OTHER string (important! if we're checking g, we need to see if
            # it occurred in secret, NOT guess. And vice versa), we need to increment
            # the cows count by 1. The cows count can be incremented by 2 on each
            # loop, if both s and g were found previously in the opposite string...
            # If we incremented it, we remove that letter from the opposite string's
            # dictionary.

            # If g or s was not found previously, simply add that letter to the dictionary
            # normally (not to the opposite string)

            # Check if the letter g occurred previously in secret. If yes,
            # we add 1 to cow, and remove that g letter from s_dic:
            if s_dic[g] > 0:
                cows += 1
                s_dic[g] -= 1
            # If not, we add letter g to the g_dic instead:
            else:
                g_dic[g] += 1

            # Do the same, except other way around!
            if g_dic[s] > 0:
                cows += 1
                g_dic[s] -= 1
            else:
                s_dic[s] += 1

    return "{}A{}B".format(bulls, cows)
