from collections import Counter


def first_non_repeating_char(s):
    """Finds the first non-repeating character in a string."""
    char_count = Counter(s)

    for char in s:
        if char_count[char] == 1:
            return char

    return None


s = "swiss"
result = first_non_repeating_char(s)
print("First non-repeating character:", result)
