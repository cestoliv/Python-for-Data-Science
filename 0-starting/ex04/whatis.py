import sys


def is_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


if len(sys.argv) < 2:
    exit(0)

assert len(sys.argv) <= 2, "more than one argument are provided"
assert is_int(sys.argv[1]), "argument is not an integer"

if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
