import time


def timer(func_to_measure, *args, **kwargs):
    """
    The timer function measures the time it takes for a wanted function to run.
    :param func_to_measure: function to measure
    :param args: list of arguments
    :param kwargs: list of keyword arguments
    :return (float): The time it took for the function to run.
    """
    start = time.time()
    func_to_measure(*args, **kwargs)
    end = time.time()
    return end - start


print(timer(print, "Hello"))
print(timer(zip, [1, 2, 3], [4, 5, 6]))
print(timer("Hi {name}".format, name="Bug"))
