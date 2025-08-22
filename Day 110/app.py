def is_possible(boards, painters, max_time):
    total = 0
    count = 1

    for length in boards:
        total += length
        if total > max_time:
            count += 1
            total = length
            if count > painters:
                return False
    return True


def painter_partition(boards, painters):
    low = max(boards)
    high = sum(boards)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_possible(boards, painters, mid):
            result = mid
            high = mid - 1
        else:
            low = mid + 1

    return result


boards = [10, 20, 30, 40]
painters = 2

print("Minimum time to paint all boards:", painter_partition(boards, painters))
