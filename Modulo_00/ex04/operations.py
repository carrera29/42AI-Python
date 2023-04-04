import sys

if len(sys.argv) is 3:
    try:
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print("Sum:         ", (num1 + num2))
        print("Difference:  ", (num1 - num2))
        print("Product:     ", (num1 * num2))
        if num2 is not 0:
            print("Quotient:    ", (num1 / num2))
            print("Remainder:   ", (num1 % num2))
        else:
            print("Error division by zero\nError modulo by zero")
    except:
        print("Error: only integers")