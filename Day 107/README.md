# 🎯 Day #107 of My 365 Days Coding Challenge

## 💭 Reflection

Today I explored **probabilistic data structures** and implemented a **Bloom Filter** 🌸. Unlike a normal set, this structure trades off **accuracy for memory efficiency**:

* ✅ **No false negatives** → if it says an item is *not* present, it’s 100% correct
* ⚠️ **Possible false positives** → it may say something *is present* even if it’s not

This makes Bloom Filters perfect for large-scale applications where memory is precious and occasional false positives are acceptable (e.g., **databases, caches, spam filters**).

---

## 📚 What I Did

* Implemented a **Bloom Filter in Python**
* Used **bit array** and **multiple hash functions** (via `hashlib`)
* Added elements and checked membership efficiently

---

## 📝 Implementation

```python
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
```

---

## 💡 Key Learnings

* Bloom Filters use **bit arrays + hash functions** for compact set representation.
* They’re **fast and memory efficient**, widely used in **big data systems**.
* **Trade-offs:**

  * ✅ Scalable, low memory footprint
  * ⚠️ False positives possible
* Tuning the **bit array size** and **number of hashes** controls the false positive rate.

---

## 🚀 Next Steps

* 📈 Implement formulas to calculate **optimal size & hash count**
* 🔄 Extend to **Counting Bloom Filter** (supports deletions)
* ⚡ Apply in **real-world use cases** like:

  * Duplicate detection in search engines
  * Caches and DB query optimization
  * Network filtering and anti-spam systems

---

\#365DaysOfCode #BloomFilter #ProbabilisticDataStructures #Hashing #BigData #EfficientAlgorithms #Python #CodingChallenge #InterviewPrep #AlgoMagic
