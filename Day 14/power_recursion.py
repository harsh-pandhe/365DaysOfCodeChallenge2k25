def power(base, exp):
    if exp == 0:
        return 1
    elif exp < 0:
        return 1 / power(base, -exp)
    return base * power(base, exp - 1)

base = int(input("Enter the base: "))
exp = int(input("Enter the exponent: "))
print(f"{base} raised to the power of {exp} is: {power(base, exp)}")