def celsius_to_fahrenheit(celsius):
    return (celsius * 9 / 5) + 32


def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5 / 9


while True:
    print("\nTemperature Converter 🌡️")
    print("1: Celsius to Fahrenheit")
    print("2: Fahrenheit to Celsius")
    print("0: Exit")

    choice = input("Choose an option (1, 2, or 0): ")
    if choice == "0":
        print("Goodbye! 🌟")
        break
    elif choice == "1":
        celsius = float(input("Enter temperature in Celsius: "))
        print(f"{celsius}°C is equal to {celsius_to_fahrenheit(celsius):.2f}°F")
    elif choice == "2":
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        print(f"{fahrenheit}°F is equal to {fahrenheit_to_celsius(fahrenheit):.2f}°C")
    else:
        print("Invalid choice! Please try again.")
