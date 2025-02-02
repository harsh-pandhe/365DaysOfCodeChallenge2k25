def find_duplicates(arr):
    seen = set()
    duplicates = set()

    for num in arr:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)

    return list(duplicates)


array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
duplicates = find_duplicates(array)

print(
    f"Duplicate elements in the array: {duplicates}"
    if duplicates
    else "No duplicates found."
)
