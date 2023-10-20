import random
some_string = input("Enter a string:")
i = 5
while i > 0:
    out_list = list(some_string)
    random.shuffle(out_list)
    print("".join(out_list))
    i -= 1
