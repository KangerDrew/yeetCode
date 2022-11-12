# Can use recursion, but it's more intuitive to use stack data structure
# approach.

def decodeStringOneStack(s):

    # Use python's list as a stack:
    stack = []

    for ch in s:

        if ch != ']':
            stack.append(ch)
        else:

            to_process = ""

            while stack[-1] != '[':
                to_process = stack.pop() + to_process

            stack.pop()
            multiply_val = ''
            while stack and stack[-1].isdigit():
                multiply_val = stack.pop() + multiply_val

            # # The proper way to do it would be to add each letter one by one
            # # back to the stack, but we can instead append the entire
            # # to_process string to the stack instead...
            # to_process = int(multiply_val) * to_process
            #
            # for sub_ch in to_process:
            #     stack.append(sub_ch)

            stack.append(int(multiply_val) * to_process)

    return "".join(stack)


print(decodeStringOneStack("2[abc]3[cd]ef"))
