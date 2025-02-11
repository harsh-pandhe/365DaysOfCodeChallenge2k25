def evaluate_postfix(expression):
    stack = []

    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()
            a = stack.pop()

            if char == "+":
                stack.append(a + b)
            elif char == "-":
                stack.append(a - b)
            elif char == "*":
                stack.append(a * b)
            elif char == "/":
                stack.append(a / b)
            elif char == "^":
                stack.append(a**b)

    return stack[0]


expressions = [
    "3 4 + 2 * 7 /",
    "5 1 2 + 4 * + 3 -",
]

for exp in expressions:
    print(f"Postfix: {exp} → Result: {evaluate_postfix(exp)}")
