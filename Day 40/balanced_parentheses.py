def is_balanced(expression):
    stack = []
    pairs = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in "({[":
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:
                return False

    return len(stack) == 0


expressions = [
    "(a + b) * (c - d)",
    "{[()]}()",
    "{[(])}",
    "((())",
]

for exp in expressions:
    print(f"{exp}: {'Balanced' if is_balanced(exp) else 'Not Balanced'}")
