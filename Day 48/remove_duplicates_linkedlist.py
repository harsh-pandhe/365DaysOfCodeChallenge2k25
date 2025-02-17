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
