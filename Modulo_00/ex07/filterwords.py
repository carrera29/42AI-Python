import sys

output = []
if len(sys.argv) is 3:
    try:
        str = (str(sys.argv[1]).replace(",", "")).split(" ")
        num = int(sys.argv[2])
        for word in str:
            if len(word) > num:
                output.append(word)
        print (output)
    except:
        print ("Error: wrong type of arg")
else:
    print ("Error: number of arg")