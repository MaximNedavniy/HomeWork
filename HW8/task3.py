from functools import reduce


def make_operation(operator, *num: int):
    if operator == "+":
        return reduce(lambda x, y: x + y, num)
    elif operator == "-":
        return reduce(lambda x, y: x - y, num)
    else:
        return reduce(lambda x, y: x * y, num)


print(make_operation("-", 7, 6))
