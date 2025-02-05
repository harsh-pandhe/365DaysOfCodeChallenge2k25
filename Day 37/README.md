# 🎯 Day #37 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Remember those childhood days when we used to flip a book and read it backward, just for fun? 📖 Today’s challenge reminded me of that—**reversing a linked list!** It’s a fundamental problem in data structures that improves our understanding of pointers and memory manipulation.  

## 📚 What I Did Today  
I implemented a function to **reverse a singly linked list** using an iterative approach.  

### 🔹 Iterative Approach  
This method efficiently reverses the linked list using **O(n) time** and **O(1) space**.  

```python
# reverse_linked_list.py
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next
        current.next = prev
        prev = current
        current = next_node

    return prev

def print_linked_list(head):
    current = head
    while current:
        print(current.value, end=" -> ")
        current = current.next
    print("None")

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
print("Original Linked List:")
print_linked_list(head)

reversed_head = reverse_linked_list(head)
print("\nReversed Linked List:")
print_linked_list(reversed_head)
```

## 💡 Key Learning  
- **Pointer Manipulation**: The core of reversing a linked list is carefully adjusting `.next` pointers.  
- **Iterative vs. Recursive Approach**:  
  - **Iterative**: **O(n) time & O(1) space**.  
  - **Recursive**: Uses **O(n) space** due to the call stack.  

## ✨ Extra Touch  
### 🔹 Recursive Approach for Reversal  
A more elegant, recursive solution:  

```python
def reverse_linked_list_recursive(head, prev=None):
    if not head:
        return prev
    next_node = head.next
    head.next = prev
    return reverse_linked_list_recursive(next_node, head)
```

### 🔹 Edge Cases Considered  
✅ Empty list (`None`).  
✅ Single node (`1 -> None`).  
✅ Already reversed list (`5 -> 4 -> 3 -> 2 -> 1`).  

## 🚀 Your Turn  
Can you extend this to **reverse in groups of K** instead of the whole list?  

---

#365DaysOfCode #CodingChallenge #ReverseLinkedList  