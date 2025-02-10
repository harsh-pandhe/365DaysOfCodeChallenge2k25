def precedence(op):
    if op in ("+", "-"):
        return 1
    if op in ("*", "/"):
        return 2
    if op in ("^"):
        return 3
    return 0


def infix_to_postfix(expression):
    output = []
    stack = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == "(":
            stack.append(char)
        elif char == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and precedence(stack[-1]) >= precedence(char):
                output.append(stack.pop())
            stack.append(char)

    while stack:
        output.append(stack.pop())

    return "".join(output)


expressions = ["a+b*(c^d-e)^(f+g*h)-i", "A*(B+C)/D", "(X+Y*Z)^W"]
for exp in expressions:
    print(f"Infix: {exp} → Postfix: {infix_to_postfix(exp)}")
