def name(fn, ln):
    """
    Return a full name, given a first and last name.
    :param fn: first name
    :param ln: last name
    :return: full name, capitalized
    """
    return (fn + ' ' + ln).title()


def name_cond(fn, ln, min_len):
    """
    :param fn: first name
    :param ln: last name
    :param min_len: minimum length of the full name
    :return: True if the name is long enough, False otherwise
    """
    return min_len == -1 or (0 < min_len <= len(fn) + len(ln))


def full_names(first_names, last_names, min_length=-1):
    """
    Return a list of full names, given a list of first names and a list of last names.
    :param first_names: list of first names
    :param last_names: list of last names
    :param min_length:  minimum length of the full name
    :return: list of full names
    """
    return [name(first, last) for first in first_names for last in last_names if name_cond(first, last, min_length)]


firsts = ['avi', 'moshe', 'yaakov']
lasts = ['cohen', 'levi', 'mizrahi']
print(full_names(firsts, lasts, 10))
