def power_set(s):
    """Returns the power set of a given set."""
    if not s:
        return [[]]

    rest = power_set(s[1:])
    return rest + [[s[0]] + subset for subset in rest]


my_set = [1, 2, 3]
print("Original Set:", my_set)
print("Power Set:", power_set(my_set))
