def binary_search_recursive(arr, target, low, high):
    if low > high:
        return -1
    mid = (low + high) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] > target:
        return binary_search_recursive(arr, target, low, mid - 1)
    else:
        return binary_search_recursive(arr, target, mid + 1, high)


array = list(
    map(int, input("Enter the sorted array elements separated by spaces: ").split())
)
target = int(input("Enter the target value to search: "))
result = binary_search_recursive(array, target, 0, len(array) - 1)
print(
    f"Element found at index {result}"
    if result != -1
    else "Element not found in the array."
)
