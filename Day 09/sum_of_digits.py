def sum_of_digits(n):
    n = abs(n)
    total = 0
    while n > 0:
        total += n % 10
        n //= 10
    return total


num = int(input("Enter a number: "))
print(f"The sum of the digits in {num} is: {sum_of_digits(num)}")
