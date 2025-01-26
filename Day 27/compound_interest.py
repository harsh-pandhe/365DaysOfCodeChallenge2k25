def calculate_compound_interest(principal, rate, time, n):
    # Formula: A = P * (1 + r/n)^(n*t)
    amount = principal * (1 + rate / (n * 100)) ** (n * time)
    compound_interest = amount - principal
    return compound_interest, amount


P = float(input("Enter the principal amount: "))
R = float(input("Enter the annual interest rate (in %): "))
T = float(input("Enter the time (in years): "))
N = int(input("Enter the number of times interest is compounded per year: "))

CI, total_amount = calculate_compound_interest(P, R, T, N)
print(f"Compound Interest: {CI:.2f}")
print(f"Total Amount: {total_amount:.2f}")
