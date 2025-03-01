def bubble_sort(arr):
    """Sorts an array using Bubble Sort algorithm."""
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break


arr = [64, 25, 12, 22, 11]
print("Original Array:", arr)
bubble_sort(arr)
print("Sorted Array:", arr)
