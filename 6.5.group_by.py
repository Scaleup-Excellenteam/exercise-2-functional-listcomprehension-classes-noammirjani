def group_by(func, iters):
    """Group the elements of a list based on a function.
    :param func:  function to group by
    :param iters:   list of elements
    :return:      dictionary of grouped elements
    """
    result = {}
    for x in iters:
        key = func(x)
        if key in result:
            result[key].append(x)
        else:
            result[key] = [x]
    return result


print(group_by(len, ["hi", "bye", "yo", "try"]))
