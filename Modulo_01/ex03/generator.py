import random

def generator(text, sep, option=None):
    """     Divide el texto de acuerdo al valor de sep y producirá las sub-strings.
                option especifica si una acción se realizará sobre las sub-strings antes de ser producidas.
    """
    result = text.split(sep)
    aux = []
    if option == "ordered":
        while result:
            word = min(result)
            result.remove(word)
            yield word
    elif option == "uniqued":
        for word in result:
            if word not in aux:
                aux.append(word)
                yield word
    elif option == "shuffle":
        while result:
            num = random.randint(0, len(result) -1)
            yield result[num]
            del result[num]
    else:
        for word in result:
            yield word

text = "Le Lorem Ipsum est simplement du faux texte."
sep = " "

for word in generator(text, sep, "shuffle"):
    print(word)