import random
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

def quicksort(arr, partition_limit=10):
    if len(arr) <= partition_limit:
        insertion_sort(arr)
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        arr[:] = left + middle + right
        quicksort(left, partition_limit)
        quicksort(right, partition_limit)



random_list = random.sample(range(1, 100), 10)
print("Original list:", random_list)

partition_limit_value = 10
quicksort(random_list, partition_limit=partition_limit_value)
print(f"Sorted list with partition limit {partition_limit_value}:", random_list)
