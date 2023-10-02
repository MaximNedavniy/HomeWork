import random
some_list = []
while True:
    some_list.append(random.randint(0, 100))
    if len(some_list) == 10:
        break
print(f"List: {some_list} Maximum number: {max(some_list)}")
