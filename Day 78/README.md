# 🎯 Day #78 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Today, I explored **Edit Distance (Levenshtein Distance)**—a fundamental problem in **Dynamic Programming**!  
This algorithm helps measure how different two strings are by counting the **minimum operations** (insertions, deletions, or substitutions) needed to convert one string into another.  

This challenge enhanced my **DP problem-solving skills**, especially for **text similarity, spell-checking, and NLP applications**.  

---

## 📚 What I Did Today  
I implemented **Edit Distance** using **bottom-up DP (Tabulation)** with **O(m * n) time complexity**.  

---

## 📝 **Edit Distance (Levenshtein Distance) – Dynamic Programming**  

```python
def edit_distance(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(m + 1):
        dp[i][0] = i  
    for j in range(n + 1):
        dp[0][j] = j  

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i - 1] == s2[j - 1]:  
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j],   
                                   dp[i][j - 1],    
                                   dp[i - 1][j - 1]) 

    return dp[m][n]

s1 = "kitten"
s2 = "sitting"
print("Edit Distance:", edit_distance(s1, s2))
```

---

## 💡 Key Learnings  
✅ **Dynamic Programming (Bottom-Up)** ensures efficiency (**O(m * n)** complexity).  
✅ **Three Operations Considered:**  
   🔹 **Insert** a character  
   🔹 **Delete** a character  
   🔹 **Replace** a character  
✅ **Base Cases:** If one string is empty, we must insert/delete all characters from the other.  
✅ **Used in NLP, spell-checking, and DNA sequence analysis!**  

---

## 🚀 Your Turn  
Can you optimize this using **space-efficient DP (O(n) space)?**  

#365DaysOfCode #CodingChallenge #EditDistance #DynamicProgramming #NLP #TextProcessing  