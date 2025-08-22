def two_sum(nums, target):
    hashmap = {}
    for i, num in enumerate(nums):
        diff = target - num
        if diff in hashmap:
            return [hashmap[diff], i]
        hashmap[num] = i
    return []


nums = [2, 7, 11, 15]
target = 9
print("2-Sum Result:", two_sum(nums, target))
