def permute(s, chosen=""):
    if len(s) == 0:
        print(chosen)
        return

    for i in range(len(s)):
        remaining = s[:i] + s[i + 1 :]
        permute(remaining, chosen + s[i])


word = "ABC"
permute(word)
