def find_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

array1 = list(
    map(int, input("Enter the first array elements separated by spaces: ").split())
)
array2 = list(
    map(int, input("Enter the second array elements separated by spaces: ").split())
)

intersection = find_intersection(array1, array2)
print(f"Intersection of the two arrays: {intersection}")
