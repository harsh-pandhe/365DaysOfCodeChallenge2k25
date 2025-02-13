class ListNode:
    def __init__(self, value=0, next=None):
        self.value = value
        self.next = next


def merge_sorted_lists(l1, l2):
    if not l1:
        return l2
    if not l2:
        return l1

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
