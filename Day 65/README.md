# 🎯 Day #65 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
I always thought the **Tower of Hanoi** was just a fun puzzle, but today, I realized it’s a **perfect recursion problem**! It teaches problem-solving, recursion depth, and the power of breaking big problems into smaller ones. 🔥  

## 📚 What I Did Today  
I implemented a **recursive solution** to solve the **Tower of Hanoi** problem for `N` disks. It moves all disks from the **source peg** to the **destination peg** using an **auxiliary peg**—all while following the classic rules.  

---

### 📝 **Tower of Hanoi Implementation**  

```python
def tower_of_hanoi(n, source, auxiliary, destination):
    if n == 1:
        print(f"Move disk 1 from {source} to {destination}")
        return
    
    tower_of_hanoi(n - 1, source, destination, auxiliary)
    print(f"Move disk {n} from {source} to {destination}")
    tower_of_hanoi(n - 1, auxiliary, source, destination)

n = 3
tower_of_hanoi(n, 'A', 'B', 'C')
```

---

## 💡 Key Learning  
✅ **How the Algorithm Works:**  
1. Move `N-1` disks from **source** → **auxiliary** peg  
2. Move the **largest disk** directly to **destination** peg  
3. Move `N-1` disks from **auxiliary** → **destination** peg  

✅ **Time Complexity:**  
- The recurrence relation is **T(n) = 2T(n-1) + 1**  
- This gives **O(2^n) exponential complexity**  

✅ **Why It’s Fascinating?**  
- It’s a **classic recursion problem** 🧠  
- Teaches **divide & conquer** 🔥  
- Used in **computer science, robotics, and AI**  

---

## ✨ Extra Touch  
🚀 **Real-World Applications of Tower of Hanoi:**  
- **Recursion & Algorithm Design**  
- **File Backup Systems** (Incremental backups)  
- **Hanoi Networks** (Parallel computing concepts)  

---

## 🚀 Your Turn  
Have you ever solved Tower of Hanoi manually? Try running this code and see **how recursion magically solves it**! 🔥  

#365DaysOfCode #CodingChallenge #Recursion #TowerOfHanoi #Python  