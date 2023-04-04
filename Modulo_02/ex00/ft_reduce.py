def ft_reduce(function_to_apply, iterable):
    """Apply function of two arguments cumulatively.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    A value, of same type of elements in the iterable parameter.
    None if the iterable can not be used by the function.
    """

    result = iterable[0]
    for item in iterable[1:]:
        result = function_to_apply(result, item)
    return result

lst = ('H', 'e', 'l', 'l', 'o', ' ', 'w', 'o', 'r', 'l', 'd')
lst2 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
print (ft_reduce(lambda u, v: u + v, lst))
print (ft_reduce(lambda u, v: u + v, lst2))
print (ft_reduce(lambda u, v: u + v,[]))