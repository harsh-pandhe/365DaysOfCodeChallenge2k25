class FenwickTree:
    def __init__(self, size):
        self.n = size
        self.tree = [0] * (self.n + 1)

    def update(self, i, delta):
        i += 1
        while i <= self.n:
            self.tree[i] += delta
            i += i & -i  # Move to parent

    def prefix_sum(self, i):
        i += 1
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i  # Move to ancestor
        return result

    def range_sum(self, left, right):
        return self.prefix_sum(right) - self.prefix_sum(left - 1)


arr = [1, 3, 5, 7, 9, 11]
bit = FenwickTree(len(arr))

for i in range(len(arr)):
    bit.update(i, arr[i])

print("Prefix sum up to index 3:", bit.prefix_sum(3))  # 1+3+5+7 = 16
print("Range sum from 2 to 5:", bit.range_sum(2, 5))  # 5+7+9+11 = 32

# Update index 2 (value 5 -> 10)
bit.update(2, 5)
print("After update: Prefix sum up to index 3:", bit.prefix_sum(3))  # Now 21
