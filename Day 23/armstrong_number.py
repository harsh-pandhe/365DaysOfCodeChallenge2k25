def is_armstrong(number):
    digits = list(map(int, str(number)))
    power = len(digits)
    return sum(digit ** power for digit in digits) == number

def find_armstrong_numbers(start, end):
    return [num for num in range(start, end + 1) if is_armstrong(num)]


start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))
armstrong_numbers = find_armstrong_numbers(start, end)
print(f"Armstrong numbers between {start} and {end}: {armstrong_numbers}")
