def find_subsets(arr, index=0, current_subset=[]):
    if index == len(arr):
        print(current_subset)
        return

    find_subsets(arr, index + 1, current_subset)

    find_subsets(arr, index + 1, current_subset + [arr[index]])


arr = [1, 2, 3]
print("All subsets:")
find_subsets(arr)
