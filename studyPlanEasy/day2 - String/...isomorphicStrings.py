# Brand new easy problem, can use stack (array) to solve it, for my solution I
# used helper function that used dictionary:

def isIsomorphic(s, t):

    def convertString(word):

        # Initialize dictionary to keep track of what letter corresponds to
        # what number:

        mapping = {}
        count = 0
        converted = ""

        for letter in word:

            if letter in mapping:
                converted += mapping[letter]

            else:
                # Dot is required to separate cases where integer strings are
                # identical, but are actually different values"

                # ex) "va" vs "ck" both return "210", without the dot. With dot,
                # they return "2.10" and "21.0"
                converted += str(count) + "."
                mapping[letter] = str(count) + "."
                count += 1

        # Return the converted string.
        return converted

    # Two isomorphic strings should return the same results:
    return convertString(s) == convertString(t)

