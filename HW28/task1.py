def bubble_sort(data_collection):
    for i in range(len(data_collection)):

        for j in range(0, len(data_collection) - i - 1):
            if data_collection[j] > data_collection[j + 1]:
                temp = data_collection[j]
                data_collection[j] = data_collection[j + 1]
                data_collection[j + 1] = temp

        for j in range(len(data_collection) - 1, i, -1):
            if data_collection[j] < data_collection[j - 1]:
                temp = data_collection[j]
                data_collection[j] = data_collection[j - 1]
                data_collection[j - 1] = temp


my_list = [53, 25, 21, 12, 42, 15, 60]
bubble_sort(my_list)
print(my_list)
