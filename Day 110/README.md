# 🚀 Day #110 of My 365 Days Coding Challenge

This project contains a **Python implementation** of the classic **Painter’s Partition Problem**, solved using a **binary search on the answer** combined with a **greedy validation check**.

---

## 📖 Problem Statement

You have **N boards** of different lengths and **K painters**. Each painter paints **contiguous boards**, and the goal is to **minimize the maximum time** taken by any single painter.

**Key challenge:** Find the optimal partitioning of boards so that the workload is balanced.

---

## 🧠 Approach

1. **Binary Search on Answer**

   * The minimum possible time = the **longest board**
   * The maximum possible time = **sum of all boards**

2. **Greedy Check Function**

   * Given a max time, simulate assigning boards to painters.
   * If more painters are required than available → not possible.
   * Otherwise → feasible partition.

3. Narrow down the result with binary search until the **minimum feasible max time** is found.

---

## 📝 Implementation

```python
def is_possible(boards, painters, max_time):
    total = 0
    count = 1

    for length in boards:
        total += length
        if total > max_time:
            count += 1
            total = length
            if count > painters:
                return False
    return True


def painter_partition(boards, painters):
    low = max(boards)
    high = sum(boards)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(boards, painters, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


boards = [10, 20, 30, 40]
painters = 2

print("Minimum time to paint all boards:", painter_partition(boards, painters))
```

---

## ⏱️ Complexity

* **Time Complexity:** `O(N log S)`

  * N = number of boards
  * S = sum of board lengths
* **Space Complexity:** `O(1)`

---

## 📊 Example

For **boards = \[10, 20, 30, 40]** and **2 painters**:

* Partition → `[10, 20, 30] | [40]`
* Maximum time = `60`
* This is the **minimum possible maximum workload** ✅

---

## 🚀 Extensions

* Generalize for **K painters** and very large input sizes
* Add **time per unit board** to simulate varying painting speeds
* Adapt into **Book Allocation Problem** (same concept, different use-case)
* Visualize partitions with **charts or animations**

---

## 🏷️ Tags

\#BinarySearch #GreedyAlgorithm #Optimization #PainterPartition #Python #DSA #InterviewPrep
