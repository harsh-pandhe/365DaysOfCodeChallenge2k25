# 🎯 Day #44 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Merging things is easy, right? Just like combining playlists or blending smoothies? 🍹 Well, in coding, merging **linked lists** efficiently is a whole different game! 😵‍💫 Today, I implemented a **function to merge two sorted linked lists**, an essential concept for **data structures and algorithms interviews**.  

## 📚 What I Did Today  
I wrote a **recursive** and an **iterative** approach to merge two **sorted** linked lists into a single sorted list. The key here is to maintain the order while efficiently combining nodes.  

### 📝 **Merging Two Sorted Linked Lists**  

```python
# merge_sorted_linked_lists.py
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def merge_sorted_lists(l1, l2):
    if not l1: return l2
    if not l2: return l1

    if l1.value < l2.value:
        l1.next = merge_sorted_lists(l1.next, l2)
        return l1
    else:
        l2.next = merge_sorted_lists(l1, l2.next)
        return l2

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head):
    while head:
        print(head.value, end=" -> ")
        head = head.next
    print("None")

list1 = create_linked_list([1, 3, 5])
list2 = create_linked_list([2, 4, 6])

print("List 1:")
print_linked_list(list1)

print("List 2:")
print_linked_list(list2)

merged = merge_sorted_lists(list1, list2)

print("Merged List:")
print_linked_list(merged)
```

## 💡 Key Learning  
- **Recursion makes merging intuitive**, but an **iterative approach** (using a dummy node) can save memory.  
- **Linked lists are powerful**, but working with them requires careful pointer management.  
- **Time Complexity:** **O(n + m)**, where `n` and `m` are the lengths of the lists.  

## ✨ Extra Touch  
✅ **Supports merging of any two sorted lists**  
✅ **Can be adapted to merge k sorted lists (Heap-based approach)**  
✅ **Try implementing this iteratively with a dummy node!**  

## 🚀 Your Turn  
Modify this to handle **unsorted lists** by sorting them first before merging!  

---

#365DaysOfCode #CodingChallenge #LinkedLists  