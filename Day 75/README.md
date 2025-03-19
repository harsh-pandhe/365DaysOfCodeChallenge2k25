# 🎯 Day #75 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Today, I tackled one of the most famous backtracking problems—**the N-Queens problem**! 👑♟️ This challenge involves placing **N queens on an N×N chessboard** such that no two queens attack each other. Learning **backtracking** through this problem gave me a deeper appreciation for **recursion, constraint satisfaction, and pruning unnecessary computations**.  

## 📚 What I Did Today  
I implemented a **backtracking-based solution** to generate all possible valid N-Queens placements.  

---

## 📝 **N-Queens Solution (Backtracking Approach)**  

```python
def print_board(board):
    for row in board:
        print(" ".join(row))
    print("\n")

def is_safe(board, row, col, n):
    for i in range(row):
        if board[i][col] == "Q":
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == "Q":
            return False

    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == "Q":
            return False

    return True

def solve_n_queens(board, row, n):
    if row == n:
        print_board(board)
        return True  

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = "Q" 
            solve_n_queens(board, row + 1, n)
            board[row][col] = "." 

def n_queens(n):
    board = [["." for _ in range(n)] for _ in range(n)]
    solve_n_queens(board, 0, n)

n = 8
n_queens(n)
```

---

## 💡 Key Learnings  
✅ **Backtracking** helps efficiently explore all possibilities by pruning invalid paths early.  
✅ **Constraint Checking:** Instead of placing queens randomly, I validated each move against **column & diagonal constraints**.  
✅ **Time Complexity:** The worst case is **O(N!)**, but pruning greatly improves efficiency.  

---

## 🚀 Your Turn  
Modify this implementation to **return all possible valid solutions** instead of printing them.  

#365DaysOfCode #CodingChallenge #Backtracking #NQueens #Algorithms  