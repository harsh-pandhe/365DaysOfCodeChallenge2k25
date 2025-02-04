def remove_duplicates(string):
    seen = set()
    result = []

    for char in string:
        if char not in seen:
            seen.add(char)
            result.append(char)

    return "".join(result)


string = input("Enter a string: ")
print(f"String after removing duplicates: {remove_duplicates(string)}")
