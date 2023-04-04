import string
import sys

def text_analyzer(text):
    '''
    This function counts the number of upper characters, lower characters,
    punctuation and spaces in a given text.\n'''
    upp = 0
    low = 0
    sig = 0
    spa = 0
    if isinstance(text, str):
        if text is None or len(text) is 0:
            text = input('What is the text to analyze?\n')
        for c in text:
            if c.isupper():
                upp = upp + 1
            elif c.islower():
                low = low + 1
            elif c in string.punctuation:
                sig = sig + 1
            elif c.isspace():
                spa = spa + 1
        print (f"""
        - {upp} upper letter(s)
        - {low} lower letter(s)
        - {sig} punctuation mark(s)
        - {spa} space(s)\n""")
    else:
        print ("Error: argument is not a string\n")

if __name__ == '__main__':
    if len(sys.argv) is 2:
        text_analyzer(sys.argv[1])
    else:
        print ("Error: wrong number of arguments")