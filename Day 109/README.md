# 🚀 Day #109 of My 365 Days Coding Challenge

## 📌 Topic: **K-Nearest Neighbors (k-NN) Search Using k-d Tree**

### 💭 Reflection

Today I explored something **geometrically beautiful and computationally smart** — performing a **k-nearest neighbors (k-NN) search** on a **k-d tree**. 🌍📍

While brute-force would search every point, a **k-d tree** partitions the space intelligently, letting you **prune entire regions** while still finding the closest neighbors efficiently. It felt like building a tiny GPS that thinks spatially. 🧠🗺️

---

## 📚 What I Did

* ✅ Built a **k-d tree** from a set of 2D points
* ✅ Implemented **recursive k-nearest search** with a **max-heap** to track closest neighbors
* ✅ Used **Euclidean distance** for proximity measurement

---

## 📝 Code Implementation

```python
import heapq
from math import dist

class KDNode:
    def __init__(self, point, axis, left=None, right=None):
        self.point = point
        self.axis = axis
        self.left = left
        self.right = right

def build_kd_tree(points, depth=0):
    if not points:
        return None

    axis = depth % len(points[0])
    points.sort(key=lambda x: x[axis])
    median = len(points) // 2

    return KDNode(
        point=points[median],
        axis=axis,
        left=build_kd_tree(points[:median], depth + 1),
        right=build_kd_tree(points[median + 1:], depth + 1)
    )

def knn_search(root, target, k):
    heap = []

    def recursive_search(node):
        if not node:
            return

        point = node.point
        axis = node.axis
        d = dist(point, target)

        if len(heap) < k:
            heapq.heappush(heap, (-d, point))
        elif d < -heap[0][0]:
            heapq.heappushpop(heap, (-d, point))

        diff = target[axis] - point[axis]
        close, away = (node.left, node.right) if diff < 0 else (node.right, node.left)

        recursive_search(close)
        if len(heap) < k or abs(diff) < -heap[0][0]:
            recursive_search(away)

    recursive_search(root)
    return [point for _, point in sorted(heap, reverse=True)]

points = [(2, 3), (5, 4), (9, 6), (4, 7), (8, 1), (7, 2)]
k = 3
target = (5, 5)

tree = build_kd_tree(points)
neighbors = knn_search(tree, target, k)

print(f"{k} nearest neighbors to {target}: {neighbors}")
```

---

## 💡 Key Learnings

* ✅ A **k-d tree** splits data along alternating axes (like a binary tree in multiple dimensions).
* ✅ During k-NN search:

  * Traverse recursively.
  * Track best candidates with a **max-heap**.
  * Use **backtracking and pruning** to skip irrelevant branches.

**⏱️ Time Complexity:**

* Build: **O(n log n)**
* Query: **O(log n)** on average (for small `k`)

---

## 🚀 Try It Yourself

* ➕ Extend to **3D or 4D points**.
* 🔄 Try different distance metrics (e.g., Manhattan distance).
* ⚙️ Compare **brute-force vs k-d tree performance**.

---

\#365DaysOfCode #KNN #KDTree #GeometricAlgorithms #NearestNeighbors #SpatialSearch #PythonCoding #AlgoChallenge #MachineLearningTools #InterviewPrep
