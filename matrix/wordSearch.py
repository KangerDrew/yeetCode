from collections import Counter


# My first attempt at word search problem, too slow!
def wordSearch(board, word):
    rows, columns = len(board), len(board[0])
    w_length = len(word)
    travelled = set()

    def dfsWord(row, column, index):
        if index == w_length:
            return True

        if word[index] != board[row][column]:
            return False

        travelled.add((row, column))

        possible_paths = [(row - 1, column), (row + 1, column),
                          (row, column - 1), (row, column + 1)]

        for r, c in possible_paths:
            if (r in range(rows) and
                    c in range(columns) and
                    (r, c) not in travelled
                    and dfsWord(r, c, index + 1)):
                return True

        travelled.remove((row, column))

        if index + 1 == w_length:
            return True

        return False

    for i in range(rows):

        for j in range(columns):

            if dfsWord(i, j, 0):
                return True

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

    for letter in word:
        if count[letter]:
            count[letter] -= 1
        else:
            return False

    # LEETCODE SPECIFIC PRUNING - INVALID ELSEWHERE:
    # The below "pruning" works to speed up the test case #47,
    # where we have a board filled with A's and two B's, and our
    # given string is AAAAAAAAAAAAABB. If we flip the word and
    # check starting with B first, the recursive function will not
    # run more than 1 level because there are no sections on the
    # board where there are two adjacent Bs!
    if word[0] in count and word[-1] in count:
        if count[word[0]] > count[word[-1]]:
            word = word[::-1]

    travelled = set()

    def dfs(r, c, i):
        if i == len(word):
            return True

        if (r < 0 or c < 0 or
                r >= rows or c >= columns or
                word[i] != board[r][c] or
                (r, c) in travelled):
            return False

        travelled.add((r, c))
        res = (dfs(r + 1, c, i + 1) or
               dfs(r - 1, c, i + 1) or
               dfs(r, c + 1, i + 1) or
               dfs(r, c - 1, i + 1))

        travelled.remove((r, c))
        return res

    for row in range(rows):
        for column in range(columns):
            if dfs(row, column, 0):
                return True

    return False


print(wordSearchWPruning(test_board_2, string_2))


test_counter = Counter()

test_counter["Breh"] += 23

print(test_counter)

test_counter["Breh"] -= 21

print(test_counter)

test_counter["Breh"] -= 2

print(test_counter)

