# Given a string of mathematical operation, we need to determine what the input
# operation will yield us.

# Like we learned in elementary school, first step is to complete all the
# multiplications & divisions. When we're


def calculate(s):

    # Setup:
    current_num = 0
    stored_stack = []
    operation = "+"
    possible_op = {"+", "-", "*", "/"}

    for i, letter in enumerate(s):

        if ord("0") <= ord(letter) <= ord("9"):
            current_num = current_num * 10 + int(letter)

        if letter != " " and letter in possible_op or i == len(s) - 1:
            if operation == "+":
                stored_stack.append(current_num)
            elif operation == "-":
                stored_stack.append(current_num * -1)
            elif operation == "*":
                stored_stack.append(stored_stack.pop() * current_num)
            elif operation == "/":
                stored_stack.append(stored_stack.pop() // current_num)
            operation = letter
            current_num = 0

    res = 0

    while stored_stack:
        res += stored_stack.pop()

    return res


print(calculate("14-3/2"))
