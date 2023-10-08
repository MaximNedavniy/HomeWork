list1 = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"]
dict1 = {i: list1[i - 1] for i in range(1, len(list1))}
print(dict1)
dict2 = {i: list1.index(i) + 1 for i in list1}
print(dict2)
