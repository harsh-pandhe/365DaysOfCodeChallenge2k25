def longest_common_prefix(words):
    if not words:
        return ""

    prefix = words[0]

    for word in words[1:]:
        while not word.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


words = input("Enter words separated by spaces: ").split()
print(f"Longest Common Prefix: '{longest_common_prefix(words)}'")
