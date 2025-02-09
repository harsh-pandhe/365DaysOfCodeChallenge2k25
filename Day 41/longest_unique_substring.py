def longest_unique_substring(s):
    char_set = set()
    left = max_length = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1

        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)

    return max_length


strings = ["abcabcbb", "bbbbb", "pwwkew", "abcdef", "dvdf"]
for s in strings:
    print(f"'{s}' → {longest_unique_substring(s)}")
