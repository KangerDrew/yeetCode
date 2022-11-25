# Given a string of mathematical operation, we need to determine what the input
# operation will yield us.

# Like we learned in elementary school, first step is to complete all the
# multiplications & divisions. We use stack to keep track of the numbers in the
# expression, and whenever we see "*" or "/", we pop from the most recent entry
# of the stack, do "*" or "/" to get new number and move the resulting number
# back into the stack...

# IMPORTANT: We are given that all the integers in the expressions are non-negative!
# this means that the first operation we perform will always be addition "+"


def calculate(s):

    # Variable to keep track of "current number":
    current_num = 0
    # Stack that'll have all the numbers after "*" and "/" is completed:
    stored_stack = []
    # Variable to keep track of what the operation of current_num is. As
    # mentioned in <IMPORTANT>, first operation will always be "+":
    operation = "+"
    # Set DS that has all possible operations we'll be doing in calculator.
    # This helps clean up the second if statement:
    possible_op = {"+", "-", "*", "/"}

    # Loop through each letter. We also need to check the index position
    # because we need to check if we've arrived at the end of the s input:
    for i, letter in enumerate(s):

        # If the current letter is a digit, we update the current_num:
        if ord("0") <= ord(letter) <= ord("9"):
            current_num = current_num * 10 + int(letter)

        # If the current letter is not an empty space and is a valid operator
        # OR we've reached the end of the list, we perform the most recent
        # operation on the current_num.

        # It's CRUCIAL to not use "elif", because if we've reached the end of
        # the s input, this statement will be unable to trigger because we'll
        # exit the for loop after the if statement above triggers!
        if letter != " " and letter in possible_op or i == len(s) - 1:
            if operation == "+":
                stored_stack.append(current_num)
            elif operation == "-":
                stored_stack.append(current_num * -1)
            elif operation == "*":
                stored_stack.append(stored_stack.pop() * current_num)
            elif operation == "/":
                stored_stack.append(int(stored_stack.pop() / current_num))
            operation = letter
            current_num = 0

    # Initialize a variable to return at the end:
    res = 0

    # Add all the numbers in the stack:
    while stored_stack:
        res += stored_stack.pop()

    return res


print(calculate("-14-3"))
