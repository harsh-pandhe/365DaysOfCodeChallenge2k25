def are_anagrams(str1, str2):
    return sorted(str1) == sorted(str2)


str1 = input("Enter first string: ").replace(" ", "").lower()
str2 = input("Enter second string: ").replace(" ", "").lower()

if are_anagrams(str1, str2):
    print("Yes! The strings are anagrams. ✅")
else:
    print("No! The strings are not anagrams. ❌")
