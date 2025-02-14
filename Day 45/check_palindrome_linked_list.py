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
