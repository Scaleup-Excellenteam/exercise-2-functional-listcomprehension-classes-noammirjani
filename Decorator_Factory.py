class InvalidArgumentTypeError(TypeError):
    """Exception for invalid argument type"""
    pass


class Factory(object):
    """Factory for decorators
    :param types_checkers: dict of types and decorators"""
    def __init__(self):
        self.types_checkers = {}

    def add_checker(self, type_arg, checker):
        self.types_checkers[type_arg] = checker

    def check_by_decorator(self, type_arg):
        deco = self.types_checkers.get(type_arg)
        if deco:
            return deco(type_arg)
        else:
            return None


def type_checker_decorator(expected_type):
    """Decorator for checking argument type"""
    def decorator(function):
        def wrapper(arg):
            if isinstance(arg, expected_type):
                return function(arg)
            else:
                raise InvalidArgumentTypeError(f"Expected {expected_type}, got {type(arg)}")
        return wrapper
    return decorator


int_checker = type_checker_decorator(int)
float_checker = type_checker_decorator(float)
str_checker = type_checker_decorator(str)

factory = Factory()
factory.add_checker(int, int_checker)
factory.add_checker(float, float_checker)
factory.add_checker(str, str_checker)


@int_checker
def add(x):
    return x + 1


@float_checker
def less(x):
    return x - 1.0


@str_checker
def upper(x):
    return x.upper()


try:
    print(less(1.0))
    print(add("1.0"))
except InvalidArgumentTypeError as e:
    print(str(e))
