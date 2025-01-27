def find_median_safe(numbers):
    if not numbers:
        return "Input list is empty!"
    numbers.sort()
    n = len(numbers)
    if n % 2 != 0:
        return numbers[n // 2]
    else:
        mid1 = numbers[n // 2 - 1]
        mid2 = numbers[n // 2]
        return (mid1 + mid2) / 2


numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
median = find_median_safe(numbers)
print(f"The median is: {median}")
