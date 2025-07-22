# 🎯 Day #95 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today, I explored the incredibly smart and efficient **Fenwick Tree**, also known as a **Binary Indexed Tree (BIT)** 🌲.
What amazed me most is how this structure leverages **binary representation** to perform **prefix sum queries and updates in O(log n)**.

It's a reminder that clever math and bitwise operations can lead to **powerful optimizations**, especially when working with data streams or large-scale analytics.

---

## 📚 What I Built

I implemented a **Fenwick Tree** with:

* 🧮 `update(index, delta)` — Add a value to an index.
* 📊 `prefix_sum(index)` — Get the sum from index `0` to `index`.
* 📏 `range_sum(left, right)` — Query the sum from `left` to `right` indices.

---

## 📝 Python Code – Fenwick Tree (BIT)

```python
class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)

    def update(self, i, delta):
        i += 1  # Convert to 1-based index
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i  # Move to parent

    def prefix_sum(self, i):
        i += 1  # Convert to 1-based index
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i  # Move to ancestor
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)
```

---

## ▶️ Example Usage

```python
arr = [1, 3, 5, 7, 9, 11]
bit = FenwickTree(len(arr))

for i in range(len(arr)):
    bit.update(i, arr[i])

print("Prefix sum up to index 3:", bit.prefix_sum(3))       # 1+3+5+7 = 16
print("Range sum from 2 to 5:", bit.range_sum(2, 5))         # 5+7+9+11 = 32

bit.update(2, 5)
print("After update: Prefix sum up to index 3:", bit.prefix_sum(3))  # Now 21
```

---

## 💡 Key Learnings

* ✅ **1-based indexing** is crucial for bitwise updates (`i += i & -i`).
* ✅ Memory-efficient and **fast for both updates and queries**.
* ✅ Time Complexity:

  * **Build**: O(n log n)
  * **Update**: O(log n)
  * **Query**: O(log n)
* ✅ Great for:

  * Frequency tables 📊
  * Real-time streaming data 📡
  * Inversion counting in arrays 🔄
  * Competitive programming challenges 🏁

---

## 🚀 Your Turn

Try extending this to:

* 📈 **Range updates + point queries**
* 🔢 Use it for **inversion count in an array**
* 📉 Build a **2D Fenwick Tree** for grid-based queries

---

`#365DaysOfCode` `#FenwickTree` `#BinaryIndexedTree` `#PrefixSum` `#EfficientAlgorithms` `#BitwiseMagic` `#DataStructures`

---