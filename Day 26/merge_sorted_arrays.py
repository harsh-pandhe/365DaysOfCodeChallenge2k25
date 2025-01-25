def merge_sorted_arrays(arr1, arr2):
    merged_array = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            j += 1

    merged_array.extend(arr1[i:])
    merged_array.extend(arr2[j:])

    return merged_array


arr1 = list(map(int, input("Enter the first sorted array (space-separated): ").split()))
arr2 = list(
    map(int, input("Enter the second sorted array (space-separated): ").split())
)
result = merge_sorted_arrays(arr1, arr2)
print(f"Merged sorted array: {result}")
