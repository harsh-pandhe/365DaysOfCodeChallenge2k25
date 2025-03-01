def find_missing_number(arr, n):
    """Find the missing number in an array from 1 to N"""
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(arr)
    return expected_sum - actual_sum


arr = [1, 2, 4, 5, 6]
n = 6
missing = find_missing_number(arr, n)
print("Missing Number:", missing)
