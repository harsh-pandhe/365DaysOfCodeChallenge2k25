def find_largest_in_list(numbers):
    return max(numbers)

nums = list(map(int, input("Enter numbers separated by space: ").split()))
largest = find_largest_in_list(nums)
print(f"The largest number in the list {nums} is: {largest}")
