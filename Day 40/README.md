# 🎯 Day #40 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever written a long piece of code only to get **"SyntaxError: unexpected EOF while parsing"**? 😩 Turns out, missing a closing parenthesis can break everything! Today, I tackled this problem by implementing a **Balanced Parentheses Checker**—a must-have for validating expressions in code, math, and even compilers!  

## 📚 What I Did Today  
I built a **stack-based approach** to check if an expression has balanced parentheses, including `{}`, `[]`, and `()`.  

### 📝 **Balanced Parentheses Checker Implementation**  

```python
# balanced_parentheses.py
def is_balanced(expression):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}

    for char in expression:
        if char in "({[":  
            stack.append(char)
        elif char in ")}]":
            if not stack or stack.pop() != pairs[char]:  
                return False
    
    return len(stack) == 0

expressions = [
    "(a + b) * (c - d)",  # ✅ Balanced
    "{[()]}()",           # ✅ Balanced
    "{[(])}",             # ❌ Not Balanced
    "((())",              # ❌ Not Balanced
]

for exp in expressions:
    print(f"{exp}: {'Balanced' if is_balanced(exp) else 'Not Balanced'}")
```

## 💡 Key Learning  
- **Stacks are perfect for this!** Since the last opened parenthesis must close first, a **LIFO (Last In, First Out)** approach works best.  
- **Time Complexity:** **O(n)** (we scan each character once).  
- **Edge Cases Considered:**  
  ✅ Unmatched closing brackets.  
  ✅ Extra opening brackets.  
  ✅ Empty string input.  

## ✨ Extra Touch  
- ✅ **Supports all types of brackets `{}` `[]` `()`**  
- ✅ **Works with expressions, not just brackets (e.g., `"(a + b)"`)**  
- ✅ **Can be extended for HTML/XML tag validation!**  

## 🚀 Your Turn  
Can you modify this to return the **index of the unmatched bracket** instead of just `True/False`?  

---

#365DaysOfCode #CodingChallenge #BalancedParentheses  