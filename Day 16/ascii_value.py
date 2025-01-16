def print_ascii_value():
    char = input("Enter a character: ")
    if len(char) == 1:
        print(f"The ASCII value of '{char}' is: {ord(char)}")
    else:
        print("Please enter exactly one character.")


def ascii_to_char():
    ascii_val = int(input("Enter an ASCII value: "))
    print(f"The character for ASCII value {ascii_val} is: '{chr(ascii_val)}'")


print_ascii_value()
ascii_to_char()
