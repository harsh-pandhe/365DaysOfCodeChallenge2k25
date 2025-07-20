# 🎯 Day #91 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today I dove into one of the most fundamental data structures in computer science — the **Hash Table**.
Instead of using Python’s built-in `dict`, I **built one from scratch** using **separate chaining** for collision resolution.

This experience revealed the elegant design behind what seems like magic — **constant-time lookups** made possible by smart use of arrays and hashing.

---

## 📚 What I Did

✅ Built a **Hash Table** with basic functionality:

* `put(key, value)` – Add or update a key-value pair
* `get(key)` – Retrieve the value for a key
* `remove(key)` – Delete a key-value pair
* `display()` – View the entire hash table structure

✅ Used **separate chaining** to handle collisions.

---

## 📝 Python Code – Hash Table with Separate Chaining

```python
class HashTable:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                pair[1] = value
                return
        self.table[index].append([key, value])

    def get(self, key):
        index = self._hash(key)
        for pair in self.table[index]:
            if pair[0] == key:
                return pair[1]
        return None

    def remove(self, key):
        index = self._hash(key)
        for i, pair in enumerate(self.table[index]):
            if pair[0] == key:
                del self.table[index][i]
                return True
        return False

    def display(self):
        for i, bucket in enumerate(self.table):
            print(f"Bucket {i}: {bucket}")
```

---

## ▶️ Example Usage

```python
ht = HashTable()

ht.put("name", "Harsh")
ht.put("age", 20)
ht.put("location", "India")

ht.display()

print("Name:", ht.get("name"))
print("Remove age:", ht.remove("age"))
ht.display()
```

---

## 💡 Key Learnings

* ✅ **Hashing** is the foundation of quick lookup.
* ✅ A good **hash function** spreads keys evenly across buckets.
* ✅ **Separate Chaining** handles collisions using linked lists (here, lists of lists).
* ✅ Time Complexity (average case):

  * Insert/Get/Delete: **O(1)**
  * Worst case (all in one bucket): **O(n)**

---

## 🚀 Your Turn

* 🔁 Implement **linear probing** as a collision resolution technique.
* 🔄 Add **dynamic resizing** when load factor exceeds a threshold.
* 🧪 Try using custom objects as keys by overriding `__hash__` and `__eq__`.

---

`#365DaysOfCode` `#HashTable` `#DataStructures` `#Python` `#Hashing` `#LowLevelCoding` `#ComputerScience` `#Chaining`

---
