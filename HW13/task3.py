nums1 = [1, 2, 3, 4, 5]
nums2 = [1, -2, 3, -4, 5]
def square_nums(nums):
    return [num ** 2 for num in nums]
def remove_negatives(nums):
    return [num for num in nums if num > 0]
def choose_func(nums:list, func1, func2):
    if all(el >0 for el in nums):
        func1=square_nums(nums)
        return func1
    else:
        func2=remove_negatives(nums)
        return func2

assert choose_func(nums1, square_nums, remove_negatives) == [1, 4, 9, 16, 25]

assert choose_func(nums2, square_nums, remove_negatives) == [1, 3, 5]