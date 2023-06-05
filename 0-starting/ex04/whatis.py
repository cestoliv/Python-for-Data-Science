import sys


def is_int(s):
    if s[0] in ('-', '+'):
        return s[1:].isdigit()
    return s.isdigit()


if len(sys.argv) < 2:
    exit(0)

if len(sys.argv) > 2:
    print("AssertionError: more than one argument are provided")
    exit(0)
if not is_int(sys.argv[1]):
    print("AssertionError: argument is not an integer")
    exit(0)

if int(sys.argv[1]) % 2 == 0:
    print("I'm Even.")
else:
    print("I'm Odd.")
