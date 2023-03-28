import string


def count_words(txt_str):
    """
    Count the number of words in a string
    :param txt_str: string
    :return: dictionary with words as keys and number of words as values
    """
    valid = string.ascii_letters + string.whitespace
    list_words = ''.join([c for c in txt_str if c in valid])
    return {word: len(word) for word in list_words.split()}


txt = """You see, wire telegraph is a kind of a very, very long cat.
You pull his tail in New York and his head is meowing in Los Angeles.
Do you understand this?
And radio operates exactly the same way: you send signals here, they receive them there.
The only difference is that there is no cat.
"""
print(count_words(txt))
