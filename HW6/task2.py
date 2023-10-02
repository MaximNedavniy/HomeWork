import random
some_list = []
some_list_2 = []
some_list_3 = []
while True:
    some_list.append(random.randint(0, 10))
    some_list_2.append(random.randint(0, 10))
    if len(some_list_2) == 10:
        break
some_list_3 = list(set(some_list + some_list_2))
print(f"""
List 1: {some_list},
List 2: {some_list_2},
List 3: {some_list_3}""")
