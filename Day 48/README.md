# 🎯 Day #48 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Have you ever felt like you're stuck in a loop, seeing the same things over and over again? Well, **linked lists** can have the same issue—**duplicate nodes!** Today, I tackled the problem of **removing duplicates from a linked list** and ensuring a clean, unique sequence.  

## 📚 What I Did Today  
I implemented a function to remove **duplicate nodes** from an **unsorted** linked list using **a HashSet for O(n) time complexity**.  

### 📝 **Removing Duplicates from an Unsorted Linked List**  

```python
# remove_duplicates_linkedlist.py
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, val):
        if not self.head:
            self.head = ListNode(val)
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = ListNode(val)

    def remove_duplicates(self):
        if not self.head:
            return
        
        seen = set()
        current = self.head
        prev = None
        
        while current:
            if current.val in seen:
                prev.next = current.next
            else:
                seen.add(current.val)
                prev = current
            current = current.next

    def display(self):
        temp = self.head
        while temp:
            print(temp.val, end=" -> ")
            temp = temp.next
        print("None")

ll = LinkedList()
ll.append(1)
ll.append(2)
ll.append(3)
ll.append(2)
ll.append(4)
ll.append(1)

print("Original Linked List:")
ll.display()

ll.remove_duplicates()

print("After Removing Duplicates:")
ll.display()
```

## 💡 Key Learning  
- **Using a HashSet (O(n) time complexity)** efficiently removes duplicates instead of a nested loop (O(n²)).  
- **A `prev` pointer** is needed to **bypass** duplicate nodes.  
- Works great for **unsorted** linked lists!  

## ✨ Extra Touch  
✅ **Handles duplicate values seamlessly**  
✅ **Optimized for large datasets with O(n) complexity**  
✅ **Can be extended for sorted lists using a two-pointer approach**  

## 🚀 Your Turn  
Try modifying this to **remove duplicates from a sorted linked list without using extra space!**  

---

#365DaysOfCode #CodingChallenge #LinkedList #RemoveDuplicates  
