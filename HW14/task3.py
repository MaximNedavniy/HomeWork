def arg_rules(type_: type, max_length: int, contains: list):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            for arg in args:
                if not isinstance(arg, type_):
                    print("Only str type")
                    return False
                if not len(arg) <= max_length:
                    print("The length should be 15 symbols")
                    return False
                if not all(i in arg for i in contains):
                    print(f"Must contain {contains}")
                    return False
            return result
        return wrapper
    return decorator


@arg_rules(type_=str, max_length=15, contains=['05', '@'])
def create_slogan(name: str) -> str:
    return f"{name} пьет пепси в своем новом BMW!"


assert create_slogan('johndoe05@gmail.com') is False
assert create_slogan('05years') is False
assert create_slogan('S@SH05') == 'S@SH05 пьет пепси в своем новом BMW!'
