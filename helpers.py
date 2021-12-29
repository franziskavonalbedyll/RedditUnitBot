import collections.abc


def flatten_multi_nested_list(lst: list) -> list:
    if isinstance(lst, collections.abc.Iterable):
        return [a for i in lst for a in flatten_multi_nested_list(i)]
    else:
        return [lst]
