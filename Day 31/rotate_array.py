def rotate_array(arr, k):
    n = len(arr)
    k = k % n
    return arr[-k:] + arr[:-k]


array = list(map(int, input("Enter the array elements separated by spaces: ").split()))
k = int(input("Enter the number of positions to rotate: "))

rotated_array = rotate_array(array, k)
print(f"Array after rotating by {k} positions: {rotated_array}")