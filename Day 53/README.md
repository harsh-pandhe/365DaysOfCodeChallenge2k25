# 🎯 Day #53 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Ever tried a **circular queue** in real life? Think of people standing in a line, and the first person moves to the end, shifting everyone forward. That’s exactly what **rotating a linked list** feels like!  

## 📚 What I Did Today  
I wrote a function to **rotate a linked list** by `K` positions. This means shifting nodes so that the `K`-th node becomes the new head.  

### 📝 **Rotating a Linked List by K Positions**  

```python
class ListNode:
    """A simple node class for a singly linked list."""
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def rotate_linked_list(head, k):
    """Rotates a linked list to the right by k places."""
    if not head or not head.next or k == 0:
        return head

    length = 1
    tail = head
    while tail.next:
        tail = tail.next
        length += 1

    tail.next = head

    k = k % length
    steps_to_new_head = length - k
    
    new_tail = head
    for _ in range(steps_to_new_head - 1):
        new_tail = new_tail.next

    new_head = new_tail.next
    new_tail.next = None

    return new_head

def print_list(head):
    result = []
    while head:
        result.append(str(head.val))
        head = head.next
    print(" -> ".join(result))

head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))) )
k = 2
print("Original List:")
print_list(head)

rotated_head = rotate_linked_list(head, k)
print("\nRotated List:")
print_list(rotated_head)
```

## 💡 Key Learning  
- **Turning the list into a cycle helps avoid unnecessary loops.**  
- **Using `k % length` ensures we don’t rotate more than needed.**  
- **Traversing `length - k` steps gives us the new head efficiently.**  

## ✨ Extra Touch  
✅ **Handles edge cases like `k = 0` or `k > length` properly.**  
✅ **Efficient—traverses the list only a couple of times!**  
✅ **No extra space used—just smart pointer manipulation.**  

## 🚀 Your Turn  
Modify this function to **rotate the list to the left instead of the right!**  

---

#365DaysOfCode #CodingChallenge #LinkedList #Algorithm  