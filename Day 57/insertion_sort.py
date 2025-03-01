def insertion_sort(arr):
    """Sorts an array using the Insertion Sort algorithm."""
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


arr = [12, 11, 13, 5, 6]
print("Original Array:", arr)
insertion_sort(arr)
print("Sorted Array:", arr)
