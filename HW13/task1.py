def func(args):
    name = args
    print(name)

print(func.__code__.co_nlocals)