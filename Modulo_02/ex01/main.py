def what_are_the_vars(*args, **kwargs):
    """
    ...
    """
    obj = ObjectC()
    for i, item in enumerate(args):
        setattr(obj, f"var_{i}", item)
    for key, value in kwargs.items():
        if getattr(obj, key, "Error") == "Error":
            setattr(obj, key, value)
        else:
            return None
    return obj

class ObjectC(object):
    def __init__(self):
        pass
    
def doom_printer(obj):
    if obj is None:
        print("ERROR")
        print("end")
        return
    for attr in dir(obj):
        if attr[0] != '_':
            value = getattr(obj, attr)
            print("{}: {}".format(attr, value))
    print("end")

if __name__ == "__main__":
    obj = what_are_the_vars(7)
    doom_printer(obj)
   
obj = what_are_the_vars(None, [])
doom_printer(obj)
obj = what_are_the_vars("ft_lol", "Hi")
doom_printer(obj)
obj = what_are_the_vars()
doom_printer(obj)
obj = what_are_the_vars(12, "Yes", [0, 0, 0], a=10, hello="world")
doom_printer(obj)
obj = what_are_the_vars(42, a=10, var_0="world")
doom_printer(obj)
obj = what_are_the_vars(42, "Yes", a=10, var_2="world")
doom_printer(obj)

# class Ramdon:
#     def __init__(self, name:str, first:str, num:int, ref:int):
#         self.name = name
#         self.first = first
#         self.num = num
#         self.ref = ref
    
#     def __str__(self):
#         return f"""
#             Name:           {self.name}
#             First name:     {self.first}
#             Contact:        {self.num}
#             Ref. number:    {self.ref}
#             """

# empleado1 = Ramdon("Flavia", "Platt", 622, 7)
# print (empleado1)
# info = getattr(empleado1, 'ramdon', "Error")
# if info == "Error":
#     setattr(empleado1, "random", "she loves jam")
#     print (f"   { empleado1.name} -> random: {empleado1.random}")
# else:
#     print (info)