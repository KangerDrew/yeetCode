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


