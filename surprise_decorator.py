""" study design patterns = decorator factory """
""" extra exercise: create a decorator with 2 wrappers and prints "Surprise!"""


def surprise_decorator(function):
    def wrapper():
        print("Surprise!")
        function()

    return wrapper


def say_hi():
    print("Hi")


decorate = surprise_decorator(say_hi)
decorate()