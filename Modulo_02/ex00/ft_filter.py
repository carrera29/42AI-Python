def ft_filter(function_to_apply, iterable):
    """Filter the result of function apply to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """
    iterable_type = type(iterable)
    result = iterable_type()

    if isinstance(iterable, dict):
        iterable = iterable.items()

    for element in iterable:
        if function_to_apply(element):
            if isinstance(iterable, list):
                result.append(element)
            elif isinstance(iterable, set):
                result.add(element)
            elif isinstance(iterable, dict):
                result[element[0]] = element[1]
            elif isinstance(iterable, tuple):
                result += (element, )
            else:
                raise TypeError("Unsupported iterable type")
    return result

x =(1, 2, 3, 4, 5)
result = ft_filter(lambda dum: not (dum % 2), x)
print (result)