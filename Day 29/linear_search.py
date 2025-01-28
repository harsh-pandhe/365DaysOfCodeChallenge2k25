def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1


array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
target = int(input("Enter the target value to search: "))

result = linear_search(array, target)

if result != -1:
    print(f"Element found at index {result}.")
else:
    print("Element not found in the array.")
