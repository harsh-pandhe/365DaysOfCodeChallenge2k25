# 🎯 Day #42 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever wondered how calculators evaluate expressions like **(a + b) * c**? 🤔 Today, I tackled **Infix to Postfix conversion**, a crucial step in how computers process math expressions. Understanding this makes you appreciate how programming languages interpret equations! 🧠  

## 📚 What I Did Today  
I implemented the **Shunting Yard Algorithm** (by Edsger Dijkstra) to convert an **Infix expression (human-readable)** into a **Postfix expression (machine-friendly, Reverse Polish Notation - RPN)**.  

### 📝 **Infix to Postfix Implementation**  

```python
# infix_to_postfix.py
def precedence(op):
    if op in ('+', '-'):
        return 1
    if op in ('*', '/'):
        return 2
    if op in ('^'):
        return 3
    return 0  

def infix_to_postfix(expression):
    output = []
    stack = []

    for char in expression:
        if char.isalnum():
            output.append(char)
        elif char == '(':
            stack.append(char)
        elif char == ')':
            while stack and stack[-1] != '(':
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
```

## 💡 Key Learning  
- **Postfix Notation (RPN)** removes the need for parentheses and operator precedence.  
- **Stacks make parsing expressions easy**—operators are stored until needed.  
- **Time Complexity:** **O(n)** (each character is processed once).  

## ✨ Extra Touch  
✅ **Supports multiple operators `+`, `-`, `*`, `/`, `^`**  
✅ **Handles parentheses `()` correctly**  
✅ **Can be modified to evaluate postfix expressions directly!**  

## 🚀 Your Turn  
Modify this program to **evaluate the postfix expression** after conversion!  

---

#365DaysOfCode #CodingChallenge #DataStructures  