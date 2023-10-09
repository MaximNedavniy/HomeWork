from functools import reduce
def make_operation(operator, *num:int ):
    if operator=="+":
        return print(reduce(lambda x,y:x+y, num))
    elif operator=="-":
        return print(reduce(lambda x,y:x-y, num))
    else:
        return print(reduce(lambda x,y:x*y, num))

make_operation("+", 7,6)
