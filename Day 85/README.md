# 🎯 Day #85 of My 365 Days Coding Challenge

## 💭 Personal Reflection

Today, I explored **Tries (Prefix Trees)** — a fascinating and efficient data structure for handling **string-based searches**.
Tries make operations like **autocomplete, prefix-matching, and dictionary validation** lightning-fast by breaking down strings **character by character**.

Building a trie from scratch gave me hands-on experience with **recursive data structures** and **tree traversal techniques** used in everything from **search engines** to **spell checkers**.

---

## 📚 What I Did

✅ Implemented a full **Trie (Prefix Tree)** in Python.
✅ Supported operations:

* **Insert** a word
* **Search** for a word
* **Check for prefix existence**

---

## 📝 Trie Implementation in Python

```python
class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TrieNode()
            node = node.children[ch]
        node.is_end_of_word = True

    def search(self, word):
        node = self.root
        for ch in word:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return node.is_end_of_word

    def starts_with(self, prefix):
        node = self.root
        for ch in prefix:
            if ch not in node.children:
                return False
            node = node.children[ch]
        return True


trie = Trie()
words = ["hello", "helium", "harsh", "heat", "hero"]
for word in words:
    trie.insert(word)

print(trie.search("hero"))        # ✅ True
print(trie.search("her"))         # ❌ False
print(trie.starts_with("he"))     # ✅ True
print(trie.starts_with("hi"))     # ❌ False
```

---

## 💡 Key Learnings

✅ Tries break down words into **characters**, making **prefix lookups extremely fast**
✅ Time complexity for search/insert is **O(L)** where L = length of word
✅ Excellent for:

* **Autocomplete systems**
* **Spell checking**
* **IP routing**
* **Search engines**
* **T9 predictions** on mobile phones

---

## 🚀 Your Turn

Try extending this:

* 🔄 Add **delete()** functionality
* 📃 Implement **list\_all\_with\_prefix(prefix)**
* 🌐 Use it for building **search suggestions** from a large dictionary

---

\#365DaysOfCode #CodingChallenge #Trie #PrefixTree #DataStructures #Autocomplete #SearchOptimization #Python

---
