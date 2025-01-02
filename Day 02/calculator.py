def calculator():
    print("Welcome to the Python Calculator! 🧮")
    num1 = float(input("Enter the first number: "))
    operation = input("Choose an operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    if operation == "+":
        print(f"Result: {num1} + {num2} = {num1 + num2}")
    elif operation == "-":
        print(f"Result: {num1} - {num2} = {num1 - num2}")
    elif operation == "*":
        print(f"Result: {num1} * {num2} = {num1 * num2}")
    elif operation == "/":
        if num2 != 0:
            print(f"Result: {num1} / {num2} = {num1 / num2}")
        else:
            print("Error: Division by zero is undefined!")
    else:
        print("Invalid operation. Please choose +, -, *, or /.")


calculator()
