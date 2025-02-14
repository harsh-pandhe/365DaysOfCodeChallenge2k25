# 🎯 Day #45 of My 365 Days Coding Challenge!  

## 💭 Personal Reflection  
Palindromes have always fascinated me—whether it’s words like **"madam"** or numbers like **121**. But have you ever checked if a **linked list** is a palindrome? 🤯 Today, I implemented a function to check if a linked list reads the same forward and backward!  

## 📚 What I Did Today  
I used **Floyd’s Tortoise and Hare Algorithm** 🐢🐇 to find the middle of the linked list, then reversed the second half and compared both halves for a match.  

### 📝 **Checking If a Linked List is a Palindrome**  

```python
# check_palindrome_linked_list.py
class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next

def is_palindrome(head):
    if not head or not head.next:
        return True

    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next

    prev = None
    while slow:
        temp = slow.next
        slow.next = prev
        prev = slow
        slow = temp

    left, right = head, prev
    while right:
        if left.value != right.value:
            return False
        left = left.next
        right = right.next

    return True

def create_linked_list(arr):
    if not arr:
        return None
    head = ListNode(arr[0])
    current = head
    for val in arr[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

test_list = create_linked_list([1, 2, 3, 2, 1])
print("Is Palindrome?", is_palindrome(test_list))

test_list2 = create_linked_list([1, 2, 3, 4, 5])
print("Is Palindrome?", is_palindrome(test_list2))
```

## 💡 Key Learning  
- **Floyd’s Algorithm (Fast & Slow Pointer)** finds the **middle efficiently** (**O(n)**).  
- **Reversing a Linked List** helps in comparing both halves.  
- **Time Complexity:** **O(n)**, **Space Complexity:** **O(1)** (in-place reversal).  

## ✨ Extra Touch  
✅ **Handles even and odd-length lists**  
✅ **No extra space used (modifies the list temporarily)**  
✅ **Can be extended to restore the original list after checking!**  

## 🚀 Your Turn  
Modify this to **restore the original linked list** after checking for a palindrome!  

---

#365DaysOfCode #CodingChallenge #PalindromeCheck  