# 🎯 Day #79 of My 365 Days Coding Challenge!

## 💭 Personal Reflection

Palindromes have always fascinated me! Today, I tackled the **Longest Palindromic Subsequence (LPS)** problem using **Dynamic Programming**. Unlike the **Longest Palindromic Substring**, here, we can pick non-contiguous characters while maintaining order.

This problem strengthened my **recursion and DP skills**, especially for **text processing, DNA sequence analysis, and string optimization problems**.

---

## 📚 What I Did Today

I implemented **LPS using Bottom-Up DP** (Tabulation) with **O(n²) time complexity**.

---

## 📝 **Longest Palindromic Subsequence – Dynamic Programming**

```python
def longest_palindromic_subsequence(s):
    n = len(s)
    dp = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            if s[i] == s[j]:
                dp[i][j] = 2 + dp[i + 1][j - 1]
            else:
                dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

    return dp[0][n - 1]

s = "BBABCBCAB"
print("Longest Palindromic Subsequence Length:", longest_palindromic_subsequence(s))
```

---

## 💡 Key Learnings

✅ **Dynamic Programming (Bottom-Up) ensures O(n²) efficiency**
✅ **Recursive relation:**

* If `s[i] == s[j]` → `LPS(i, j) = 2 + LPS(i+1, j-1)`
* Else → `LPS(i, j) = max(LPS(i+1, j), LPS(i, j-1))`
  ✅ **Base Case:** A single-character substring is always a palindrome (length = 1).
  ✅ **Useful for bioinformatics (DNA sequence analysis) and text compression.**

---

## 🚀 Your Turn

Can you optimize this further using **space-efficient DP (O(n) space)?**

\#365DaysOfCode #CodingChallenge #LongestPalindrome #DynamicProgramming #TextProcessing #Recursion

---