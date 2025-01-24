def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = bubble_sort(numbers)
print(f"Sorted array in ascending order (manual): {sorted_numbers}")
