def isValid(s):
    stack = []

    for bracket in s:

        if bracket == "]" and len(stack) > 0 and stack[-1] == "[":
            stack.pop()
        elif bracket == "}" and len(stack) > 0 and stack[-1] == "{":
            stack.pop()
        elif bracket == ")" and len(stack) > 0 and stack[-1] == "(":
            stack.pop()
        else:
            stack.append(bracket)

    return False if stack else True


print(isValid("]"))


def improved(s):
    stack = []
    closeToOpen = { ")": "(", "]": "[", "}": "{" }

    for c in s:
        if c in closeToOpen:
            if stack and stack[-1] == closeToOpen[c]:
                stack.pop()
            else:
                # Immediately return False when brackets do not match.
                # This is why this algorithm is better.
                return False
        else:
            stack.append(c)

    return True if not stack else False

