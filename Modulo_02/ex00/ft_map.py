import copy 

def ft_map(function_to_apply, iterable):
    """Map the function to all elements of the iterable.
    Args:
    function_to_apply: a function taking an iterable.
    iterable: an iterable object (list, tuple, iterator).
    Return:
    An iterable.
    None if the iterable can not be used by the function.
    """

    if type(iterable) == list:
        result = iterable.copy()
        for i, element in enumerate(iterable):
            result[i] = function_to_apply(element)
    elif type(iterable) == tuple:
        result = tuple(list(iterable))
        lista = list(result)
        for i in range(len(iterable) -1):
            lista[i] = function_to_apply(iterable[i])
        result = tuple(lista)
    elif type(iterable) == set:
        result = set(iterable.copy())
        for element in iterable:
            result.add(function_to_apply(element))
    else:
        raise TypeError("Tipo de colección no soportado")
    return result

x = (1, 2, 3, 4, 5)
result = ft_map(lambda dum: dum + dum, x)
result2 = list(ft_map(lambda t: t * 5, x))
print (result, result2)
