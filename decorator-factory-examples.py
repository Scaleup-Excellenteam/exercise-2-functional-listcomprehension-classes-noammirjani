""" study design patterns = decorator factory """


def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def say_hi():
    return 'hello there'


def split_string_decorator(function):
    def wrapper():
        func = function()
        splitted_string = func.split()
        return splitted_string

    return wrapper


decorate = uppercase_decorator(say_hi)
print(decorate())
decorate = split_string_decorator(say_hi)
print(decorate())


def decorator_with_arguments(function):
    def wrapper_accepting_arguments(arg1, arg2):
        print("My arguments are: {0}, {1}".format(arg1, arg2))
        function(arg1, arg2)

    return wrapper_accepting_arguments


def cities(city_one, city_two):
    print("Cities I love are {0} and {1}".format(city_one, city_two))


decorate = decorator_with_arguments(cities)
decorate("Nairobi", "Accra")

print()


def a_decorator_passing_arbitrary_arguments(function_to_decorate):
    def a_wrapper_accepting_arbitrary_arguments(*args, **kwargs):
        print('The positional arguments are', args)
        print('The keyword arguments are', kwargs)
        function_to_decorate(*args)

    return a_wrapper_accepting_arbitrary_arguments


@a_decorator_passing_arbitrary_arguments
def function_with_no_argument():
    print("No arguments here.")


function_with_no_argument()
decorate = a_decorator_passing_arbitrary_arguments(function_with_no_argument)
decorate()


class Animal:
    def speak(self):
        pass


class Dog(Animal):
    def speak(self):
        return "Woof!"


class Cat(Animal):
    def speak(self):
        return "Meow!"


class AnimalFactory:
    animal_types = {
        "dog": Dog,
        "cat": Cat
    }

    def create_animal(self, animal_type):
        animal_class = self.animal_types.get(animal_type)
        if animal_class:
            return animal_class()
        else:
            return None


# Example usage
animal_factory = AnimalFactory()

dog = animal_factory.create_animal("dog")
if dog is not None:
    print(dog.speak())  # Output: Woof!

cat = animal_factory.create_animal("cat")
if cat is not None:
    print(cat.speak())  # Output: Meow!

unknown = animal_factory.create_animal("unknown")
if unknown is None:
    print("Unknown animal type")
