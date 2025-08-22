# 🎯 Day #103 of My 365 Days Coding Challenge

## 💭 Reflection

Today’s challenge was all about combining **hashing** with algorithmic efficiency to tackle two classic problems — **2-Sum** and **3-Sum**.

What’s exciting is how drastically performance improves just by using the **right data structure**. Instead of brute force, leveraging **hash maps** allows us to shrink **O(n²)** or **O(n³)** approaches into efficient **O(n)** or **O(n²)** solutions. 🚀

---

## 📚 What I Did Today

✅ Solved the **2-Sum problem** using a hash map for instant complement lookups.

✅ Solved the **3-Sum problem** by reducing it to multiple 2-Sum searches inside a loop.

---

## 📝 2-Sum Using Hash Map – Python

```python
def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return []

# Example:
nums = [2, 7, 11, 15]
target = 9
print("2-Sum Result:", two_sum(nums, target))  # Output: [0, 1]
```

---

## 📝 3-Sum Using Hash Map – Python

```python
def three_sum(nums):
    result = set()
    nums.sort()
    for i in range(len(nums)):
        target = -nums[i]
        hashmap = {}
        for j in range(i+1, len(nums)):
            complement = target - nums[j]
            if complement in hashmap:
                triplet = tuple(sorted((nums[i], nums[j], complement)))
                result.add(triplet)
            hashmap[nums[j]] = j
    return list(result)

# Example:
nums = [-1, 0, 1, 2, -1, -4]
print("3-Sum Results:", three_sum(nums))
# Output: [[-1, -1, 2], [-1, 0, 1]]
```

---

## 💡 Key Learnings

* ✅ **Hash maps** give constant-time lookups (**O(1)**).
* ✅ **2-Sum** is the simplest complement-checking problem.
* ✅ **3-Sum** reduces to multiple **2-Sum** subproblems.
* ✅ **Time Complexity:**

  * 2-Sum → **O(n)**
  * 3-Sum → **O(n²)**

This pattern is extremely useful for **interview prep** and **real-time problem solving**.

---

## 🚀 Your Turn

Try extending this approach to:

* 🔄 The **4-Sum problem**
* ⚡ Handling **streaming data** (pairs in real-time input)
* 🛡️ Using **sets** to avoid duplicate results

---

\#365DaysOfCode #HashMapPower #TwoSum #ThreeSum #CodingChallenge #AlgoPatterns #InterviewPrep #PythonProgramming #ProblemSolving
