class TypeDecorators:
    @staticmethod
    def to_int(func):
        def wrapper(*args, **kwargs):
            return int(*args)

        return wrapper

    @staticmethod
    def to_str(func):
        def wrapper(*args, **kwargs):
            return str(*args)

        return wrapper

    @staticmethod
    def to_bool(func):
        def wrapper(*args, **kwargs):
            return bool(*args)

        return wrapper

    @staticmethod
    def to_float(func):
        def wrapper(*args, **kwargs):
            return float(*args)

        return wrapper


@TypeDecorators.to_int
def do_nothing(string: str):
    return string


@TypeDecorators.to_bool
def do_something(string: str):
    return string


assert do_nothing('25') == 25

assert do_something('True') is True
