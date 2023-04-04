import sys

rev_args = sys.argv[1:][::-1]
rev_alpha = ""
for i in rev_args:
    rev_alpha = rev_alpha + i.swapcase() + " "
print(rev_alpha)
