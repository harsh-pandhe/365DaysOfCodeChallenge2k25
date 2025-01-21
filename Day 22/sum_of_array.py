def sum_of_array_manual(arr):
    total = 0
    for num in arr:
        total += num
    return total

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
result = sum_of_array_manual(numbers)
print(f"The sum of the array elements is: {result}")