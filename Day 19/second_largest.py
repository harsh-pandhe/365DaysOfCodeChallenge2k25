def distinct_sorted_numbers(numbers):
    return sorted(set(numbers), reverse=True)


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
sorted_numbers = distinct_sorted_numbers(numbers)
if len(sorted_numbers) > 1:
    print(f"The second largest number is: {sorted_numbers[1]}")
else:
    print("No second largest number.")
