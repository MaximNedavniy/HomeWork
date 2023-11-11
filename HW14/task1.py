def logger(func):
    def wrapper(*args, **kwargs):
        print(f"{func.__name__} called {args}")
        return func
    return wrapper


@logger
def add(x, y):
    return x + y


@logger
def square_all(*args):
    return [arg ** 2 for arg in args]


square_all(4, 5)
