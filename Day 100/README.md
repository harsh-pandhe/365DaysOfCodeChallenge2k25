# 🚀 Day 100 of My 365 Days Coding Challenge 🎉💯🔥

## 💭 Reflection
Today marks **Day 100** of my coding journey — a milestone that feels surreal! 🧠  
To celebrate, I solved the **Word Ladder Problem** 🪜✨.  

This problem challenges you to transform one word into another by changing only **one letter at a time**, with each transformation being a valid word.  
It’s like **Wordle + Graph Theory** combined! 😄  

---

## 📚 What I Did Today
I implemented the **Word Ladder Problem** using **Breadth-First Search (BFS)** to ensure the shortest transformation path is found from a `beginWord` to an `endWord`, given a `wordList`.

---

## 📝 Code (Python)

```python
from collections import deque


def word_ladder(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    queue = deque([(beginWord, 1)])

    while queue:
        word, steps = queue.popleft()

        if word == endWord:
            return steps

        for i in range(len(word)):
            for c in "abcdefghijklmnopqrstuvwxyz":
                new_word = word[:i] + c + word[i + 1 :]
                if new_word in wordSet:
                    wordSet.remove(new_word)
                    queue.append((new_word, steps + 1))

    return 0


begin = "hit"
end = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

result = word_ladder(begin, end, wordList)
print("Shortest transformation length:", result)
```

---

## 💡 Key Learnings
✅ Each **word = node**, and each **valid transformation = edge**.  
✅ BFS guarantees the **shortest transformation sequence**.  
✅ **Time Complexity:** O(N × L × 26)  
  - N = number of words, L = word length.  
✅ Real-world uses: **spell-checkers, AI-driven word tools, word games**.  

---

## 🚀 Your Turn!
- Can you modify it to return the **actual transformation path**?  
- Try implementing **bidirectional BFS** for even faster results!  

---

#365DaysOfCode #Day100 #WordLadder #BFS #GraphAlgorithms #ProblemSolving #Python #CodingChallenge
