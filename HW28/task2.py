def merge_sort(list_):
    if len(list_) > 1:
        mid = len(list_) // 2

        left_half = []
        for i in range(mid):
            left_half.append(list_[i])

        right_half = []
        for i in range(mid, len(list_)):
            right_half.append(list_[i])

        merge_sort(left_half)
        merge_sort(right_half)

        i = 0
        j = 0
        k = 0

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                list_[k] = left_half[i]
                i += 1
            else:
                list_[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            list_[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            list_[k] = right_half[j]
            j += 1
            k += 1


my_list = [38, 27, 43, 3, 9, 82, 10]
merge_sort(my_list)
print(my_list)

