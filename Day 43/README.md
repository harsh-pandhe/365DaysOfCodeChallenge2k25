# 🎯 Day #43 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Remember when you first learned **BODMAS/PEMDAS** in school? 😵‍💫 It turns out that computers **don’t** evaluate expressions the same way we do! Instead, they often use **Postfix (Reverse Polish Notation - RPN)** to simplify expression evaluation.  

Today, I wrote a program to **evaluate a postfix expression**—something that forms the backbone of how calculators and compilers work!  

## 📚 What I Did Today  
I implemented **Postfix Evaluation using a Stack**. This method ensures that expressions like `"3 4 + 2 * 7 /"` get evaluated correctly as `((3+4) * 2) / 7 = 2.0`.  

### 📝 **Postfix Expression Evaluation Implementation**  

```python
# evaluate_postfix.py
def evaluate_postfix(expression):
    stack = []
    
    for char in expression.split():
        if char.isdigit():
            stack.append(int(char))
        else:
            b = stack.pop()  
            a = stack.pop()
            
            if char == '+': stack.append(a + b)
            elif char == '-': stack.append(a - b)
            elif char == '*': stack.append(a * b)
            elif char == '/': stack.append(a / b)
            elif char == '^': stack.append(a ** b)

    return stack[0]

expressions = [
    "3 4 + 2 * 7 /",  # ((3+4) * 2) / 7 = 2.0
    "5 1 2 + 4 * + 3 -"  # 5 + ((1+2) * 4) - 3 = 14
]

for exp in expressions:
    print(f"Postfix: {exp} → Result: {evaluate_postfix(exp)}")
```

## 💡 Key Learning  
- **Postfix eliminates ambiguity**—no parentheses or operator precedence needed.  
- **Stacks are crucial**: Operands are pushed, operators pop & evaluate.  
- **Time Complexity:** **O(n)** (each token is processed once).  

## ✨ Extra Touch  
✅ **Supports multiple operators (`+`, `-`, `*`, `/`, `^`)**  
✅ **Handles multi-digit numbers with `split()`**  
✅ **Easy to extend with more operations (like `%` for modulus)!**  

## 🚀 Your Turn  
Modify this to **support floating-point numbers or handle errors gracefully!**  

---

#365DaysOfCode #CodingChallenge #ReversePolishNotation  