from collections import Counter


# My first attempt at word search problem, too slow!
def wordSearch(board, word):
    rows, columns = len(board), len(board[0])
    w_length = len(word)

    # Keep track of traversed sections:
    travelled = set()

    # Below is a recursive dfs function for traversing the
    # provided board:
    def dfsWord(row, column, index):
        # Base case: if we reached the end of the word, return True
        if index == w_length:
            return True

        # If the letter at index doesn't match the letter at the current
        # position on board, return False:
        if word[index] != board[row][column]:
            return False

        # Add current position to the travelled set:
        travelled.add((row, column))

        # Below are possible routes we can take from the current
        # position - left, right, down, up:
        possible_paths = [(row - 1, column), (row + 1, column),
                          (row, column - 1), (row, column + 1)]

        # Use for loop to iterate through 4 directions:
        for r, c in possible_paths:

            # Check the following:
            # - Is the new position in range?
            # - Is the new position already in travelled set?
            # - Does recursive input return True?
            if (r in range(rows) and
                    c in range(columns) and
                    (r, c) not in travelled
                    and dfsWord(r, c, index + 1)):
                return True

        # Remove the position from travelled set to clear it out
        travelled.remove((row, column))

        # Edge case: If we didn't traverse through for loop, but are
        # already at the end of the word, return True (happens if the
        # board only consists of 1 letter)
        if index + 1 == w_length:
            return True

        # Otherwise return False:
        return False

    # Loop through each letter in the board:
    for i in range(rows):

        for j in range(columns):

            # Use dfsWord function to see if it returned True:
            if dfsWord(i, j, 0):
                return True

    # If for loop above was exited without returning True, return False:
    return False


# Test case #59
test_board_1 = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
string_1 = "ABCESEEEFS"

# Test case #47
test_board_2 = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
string_2 = "AAAAAAAAAAAAABB"


# print(wordSearch(test_board_2, string_2))


def wordSearchWPruning(board, word):
    rows, columns = len(board), len(board[0])

    # Pruning 1: Check if there's even enough words in the boards:
    if len(word) > rows * columns:
        return False

    # Pruning 2: Use python's Counter object to check if enough
    # letters exist in the board for us to be able to build the word:
    count = Counter()
    for n in range(rows):
        for m in range(columns):
            count[board[n][m]] += 1

    # Now check if there are enough letters in the matrix. If we go below
    # negative number, OR the letter doesn't exist, return False:
    for letter in word:
        if count[letter] > 0:
            count[letter] -= 1
        else:
            return False

    # We need to keep track of which section has been travelled
    travelled = set()

    # Below is a recursive dfs function to traverse the matrix:
    def dfs(r, c, i):
        # Base case: We've reached the end of the word
        if i == len(word):
            return True

        # Check the following:
        # - Are we out of bounds? If yes, return False
        # - Does the letter at current index match the letter at the
        # current position? If no, return False
        # - Did we already travel to this position? If yes, return False
        if (r < 0 or c < 0 or
                r >= rows or c >= columns or
                word[i] != board[r][c] or
                (r, c) in travelled):
            return False

        # Add the current position to the travelled set, as a tuple
        travelled.add((r, c))

        # Input 4 directions (up, down, left, right), and the next index
        # to the dfs function, and see if any return True.
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))

        # Once we finish traversing, remove the position
        # so we can use travelled set again in other iterations.
        travelled.remove((r, c))

        return res

    # Loop through each position on board, and run dfs function on them:
    for row in range(rows):
        for column in range(columns):
            if dfs(row, column, 0):
                return True

    # If the above for loop didn't return True, return False:
    return False


print(wordSearchWPruning(test_board_2, string_2))


test_counter = Counter()

test_counter["Breh"] += 23

print(test_counter)

test_counter["Breh"] -= 21

print(test_counter)

test_counter["Breh"] -= 2

print(test_counter)

