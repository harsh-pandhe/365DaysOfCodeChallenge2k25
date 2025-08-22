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
        right=build_kd_tree(points[median + 1 :], depth + 1),
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
