import math
def some_def():
    try:
        a=int(input("enter the number a:"))
        b=int(input("enter the number b:"))
        return a**2/b
    except ZeroDivisionError:
        return print(f'Value:{math.inf}')
    except ValueError:
        raise ValueError ("The value of 'a' must be a number")


print(some_def())
