def binary_search_recursive(list_, value, start=0):
    if len(list_) == 0:
        return False
    mid = len(list_) // 2
    if list_[mid] == value:
        print(f"Index:{start+mid}")
        return start + mid
    elif list_[mid] < value:
        return binary_search_recursive(list_[mid + 1:], value, start + mid + 1)
    else:
        return binary_search_recursive(list_[:mid], value, start)


def fibonacci_search(list_, target):
    size = len(list_)

    start = -1

    f0 = 0
    f1 = 1
    f2 = 1
    while (f2 < size):
        f0 = f1
        f1 = f2
        f2 = f1 + f0

    while (f2 > 1):
        index = min(start + f0, size - 1)
        if list_[index] < target:
            f2 = f1
            f1 = f0
            f0 = f2 - f1
            start = index
        elif list_[index] > target:
            f2 = f0
            f1 = f1 - f0
            f0 = f2 - f1
        else:
            return index
    if (f1) and (list_[size - 1] == target):
        return size - 1
    return None


list_ = [1, 21, 32, 4, 5]

binary_search_recursive(list_, 32)
print(fibonacci_search(list_, 21))
