def count_character_frequency_advanced(string):
    frequency = {}
    for char in string.replace(" ", "").lower():
        frequency[char] = frequency.get(char, 0) + 1
    return frequency

text = input("Enter a string: ")
frequency = count_character_frequency_advanced(text)
for char, count in frequency.items():
    print(f"'{char}' appears {count} times")
