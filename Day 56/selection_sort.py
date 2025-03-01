def selection_sort(arr):
    """Sorts an array using the Selection Sort algorithm."""
    n = len(arr)

    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        arr[i], arr[min_index] = arr[min_index], arr[i]


arr = [29, 10, 14, 37, 13]
print("Original Array:", arr)
selection_sort(arr)
print("Sorted Array:", arr)
