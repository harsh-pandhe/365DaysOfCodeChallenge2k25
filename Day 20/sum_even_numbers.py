def sum_of_evens_optimized(start, end):
    first_even = start if start % 2 == 0 else start + 1
    last_even = end if end % 2 == 0 else end - 1
    count = ((last_even - first_even) // 2) + 1
    return count * (first_even + last_even) // 2


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
result = sum_of_evens_optimized(start, end)
print(f"The sum of all even numbers between {start} and {end} is: {result}")
