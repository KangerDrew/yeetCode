# My first attempt at word search problem, not passing one of the cases...
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


# A    B    C    E
# S    F    E    S
# A    D    E    E

test_board_1 = [["A", "B", "C", "E"], ["S", "F", "E", "S"], ["A", "D", "E", "E"]]
string_1 = "ABCESEEEFS"

test_board_2 = [["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "A"],
                ["A", "A", "A", "A", "A", "A"], ["A", "A", "A", "A", "A", "B"], ["A", "A", "A", "A", "B", "A"]]
string_2 = "AAAAAAAAAAAAABB"
print(wordSearch(test_board_2, string_2))
