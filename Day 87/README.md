# 🎯 Day #87 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I built two essential data structures — **Min-Heap** and **Max-Heap** — that form the backbone of algorithms like **Dijkstra’s shortest path**, **priority queues**, **job schedulers**, and more.
It was fascinating to watch how elements bubble up and sink down to maintain the heap property using only index arithmetic!

---

## 📚 What I Did

✅ Implemented **Min-Heap** and **Max-Heap** in Python using array-based binary heap structure.
✅ Added support for core operations like `insert`, `extract`, and `peek`.

---

## 📝 Min-Heap – Python Implementation

```python
class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] < self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i):
        n = len(self.heap)
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] < self.heap[smallest]:
            smallest = left
        if right < n and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != i:
            self.heap[i], self.heap[smallest] = self.heap[smallest], self.heap[i]
            self._heapify_down(smallest)
```

---

## 📝 Max-Heap – Python Implementation

```python
class MaxHeap:
    def __init__(self):
        self.heap = []

    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)

    def extract_max(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._heapify_down(0)
        return root

    def _heapify_up(self, i):
        parent = (i - 1) // 2
        while i > 0 and self.heap[i] > self.heap[parent]:
            self.heap[i], self.heap[parent] = self.heap[parent], self.heap[i]
            i = parent
            parent = (i - 1) // 2

    def _heapify_down(self, i):
        n = len(self.heap)
        largest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and self.heap[left] > self.heap[largest]:
            largest = left
        if right < n and self.heap[right] > self.heap[largest]:
            largest = right

        if largest != i:
            self.heap[i], self.heap[largest] = self.heap[largest], self.heap[i]
            self._heapify_down(largest)
```

---

## ✅ Example Usage

```python
min_heap = MinHeap()
for num in [5, 3, 8, 1, 2]:
    min_heap.insert(num)
print("Min-Heap:", min_heap.heap)
print("Extract Min:", min_heap.extract_min())
print("After Extraction:", min_heap.heap)

max_heap = MaxHeap()
for num in [5, 3, 8, 1, 2]:
    max_heap.insert(num)
print("Max-Heap:", max_heap.heap)
print("Extract Max:", max_heap.extract_max())
print("After Extraction:", max_heap.heap)
```

---

## 💡 Key Learnings

* ✅ **Min-Heap**: Parent node ≤ children
* ✅ **Max-Heap**: Parent node ≥ children
* ✅ Uses **array-based binary tree** with:

  * Left child: `2*i + 1`
  * Right child: `2*i + 2`
  * Parent: `(i - 1) // 2`
* ✅ **Time Complexity**:

  * `Insert`: O(log n)
  * `Extract`: O(log n)
* ✅ Applications:

  * **Dijkstra’s algorithm**
  * **Priority queues**
  * **Heap sort**
  * **OS scheduling systems**

---

## 🚀 Your Turn

* 🔧 Build a **Priority Queue** on top of your heap.
* 🧮 Try implementing **Heap Sort**.
* 💥 Add support for **deleting arbitrary elements**.

---

\#365DaysOfCode #Heap #MinHeap #MaxHeap #DataStructures #PriorityQueue #BFS #Algorithms #Python

---
