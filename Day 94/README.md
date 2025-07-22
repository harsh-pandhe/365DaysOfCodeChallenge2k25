# 🎯 Day #94 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I dove into one of the most powerful and efficient data structures: the **Segment Tree** 🌲.
While it initially felt overwhelming, understanding how it recursively **divides the problem** into manageable parts made it clear and elegant.

It’s a perfect example of how breaking a problem down — and tackling it in **logarithmic layers** — brings both **performance and clarity**. ⚡

---

## 📚 What I Built

An implementation of a **Segment Tree** that supports:

* 🔨 Building the tree in **O(n)**
* 📊 Querying the **sum** of any range in **O(log n)**
* ✏️ Updating any element in **O(log n)**

---

## 📝 Python Code – Segment Tree for Range Sum Queries

```python
class SegmentTree:
    def __init__(self, arr):
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)
        self.build(arr, 0, 0, self.n - 1)

    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = arr[start]
        else:
            mid = (start + end) // 2
            self.build(arr, 2 * node + 1, start, mid)
            self.build(arr, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def update(self, idx, val, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        if start == end:
            self.tree[node] = val
        else:
            mid = (start + end) // 2
            if idx <= mid:
                self.update(idx, val, 2 * node + 1, start, mid)
            else:
                self.update(idx, val, 2 * node + 2, mid + 1, end)
            self.tree[node] = self.tree[2 * node + 1] + self.tree[2 * node + 2]

    def query(self, L, R, node=0, start=0, end=None):
        if end is None:
            end = self.n - 1

        if R < start or L > end:
            return 0
        if L <= start and end <= R:
            return self.tree[node]

        mid = (start + end) // 2
        left_sum = self.query(L, R, 2 * node + 1, start, mid)
        right_sum = self.query(L, R, 2 * node + 2, mid + 1, end)
        return left_sum + right_sum
```

---

## ▶️ Example Usage

```python
arr = [1, 3, 5, 7, 9, 11]
st = SegmentTree(arr)

print("Sum of range [1, 3]:", st.query(1, 3))

st.update(1, 10)

print("After update: Sum of range [1, 3]:", st.query(1, 3))
```

---

## 💡 Key Learnings

* ✅ A **Segment Tree** is perfect for **efficient range queries** and **frequent updates**
* ✅ Divide and conquer approach builds the tree recursively
* ✅ Time Complexity:

  * **Build:** O(n)
  * **Query:** O(log n)
  * **Update:** O(log n)
* ✅ Used in:

  * Stock price analysis 📈
  * Competitive programming 🏁
  * Game development (range stats / HP tracking) 🎮

---

## 🚀 Your Turn

Can you:

* Extend this to **Range Minimum Query (RMQ)**?
* Add support for **range updates using Lazy Propagation**?
* Make it **generic** (for product, min, max, GCD)?

---

`#365DaysOfCode` `#SegmentTree` `#RangeSum` `#Python` `#EfficientAlgorithms` `#DivideAndConquer` `#DataStructures`

---