def reverse_string(input_string):
    reversed_str = ""
    for char in input_string:
        reversed_str = char + reversed_str
    return reversed_str


original = input("Enter a string to reverse: ")
reversed_result = reverse_string(original)
print(f"The reversed string is: {reversed_result}")
