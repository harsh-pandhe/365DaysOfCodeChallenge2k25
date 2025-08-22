import hashlib
import math


class BloomFilter:
    def __init__(self, size, hash_count):
        self.size = size
        self.hash_count = hash_count
        self.bit_array = [0] * size

    def _hashes(self, item):
        result = []
        for i in range(self.hash_count):
            hash_digest = hashlib.sha256((item + str(i)).encode()).hexdigest()
            index = int(hash_digest, 16) % self.size
            result.append(index)
        return result

    def add(self, item):
        for idx in self._hashes(item):
            self.bit_array[idx] = 1

    def check(self, item):
        return all(self.bit_array[idx] for idx in self._hashes(item))


bf = BloomFilter(size=1000, hash_count=4)
words = ["apple", "banana", "orange"]

for word in words:
    bf.add(word)

print("Check 'apple':", bf.check("apple"))
print("Check 'grapes':", bf.check("grapes"))
