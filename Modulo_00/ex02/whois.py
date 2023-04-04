import sys

num = int(sys.argv[1])
if len(sys.argv) != 2:
    print ("Error: more than one argument")
elif isinstance(num, int):
    if num == 0:
        print ("I'm Zero")
    elif (num % 2 == 0):
        print ("I'm Even")
    elif (num % 2 != 0):
        print ("I'm Oven")
else:
    print ("Error: the argument is not an integer")