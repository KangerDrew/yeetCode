from collections import defaultdict

# For rules 1 & 2:
# We can use a hashset set to validate whether each row/column is valid
# sudoku. To make the algorithm runtime efficient, we will be using two
# default dictionaries (hash map), where the keys will be the index of
# column/row, and the key value will be a hash set that keeps track of
# what number was on a row/column.

# For rule 3:
# We need to figure out a way to keep track of each individual 3x3 sub-
# boxes. To do this, we divide up our 9x9 board. IMPORTANT - Notice how
# when we take the floor division 3 of the column/row index, it can tell
# us which 3x3 sub-box that coordinate belongs to (see video for visual
# explanation). Using this, we can keep track of which sub-box contains
# certain number. We will use the (row_index // 3, column_index // 3) tuple,
# for the key of our default dictionary!


def validSudoku(board):

    # Create dictionaries (hash maps) that will keep track of which
    # row/columns/boxes contain which number:
    columns = defaultdict(set)
    rows = defaultdict(set)
    boxes = defaultdict(set)

    # loop through each tile of the sudoku board. It is given that
    # the board will always be 9x9:
    for r in range(9):
        for c in range(9):

            # If the value is empty at a current position, skip:
            if board[r][c] == ".":
                continue

            # If the value already exist in the column/row/sub-box,
            # we need to return False:
            if (board[r][c] in rows[r] or
                board[r][c] in columns[c] or
                board[r][c] in boxes[(r // 3, c // 3)]):
                return False

            # Otherwise, we store the value into the hash maps:
            columns[c].add(board[r][c])
            rows[r].add(board[r][c])
            boxes[(r // 3, c // 3)].add(board[r][c])

    # If the above loop finished without returning False, it means we have
    # a valid sudoku board:
    return True

