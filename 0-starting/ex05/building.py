import sys
from string import punctuation


def main():
    """
    Take a user input or a sys.argv input and count characters,
    upper, lower, ponctuation marks, spaces and digits.
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than one argument are provided")
        exit(0)
    elif len(sys.argv) == 2:
        message = sys.argv[1]
    else:
        print("What is the text to count?")
        message = sys.stdin.readline()

    spaces = [' ', '\n']

    print(f"The text contains {len(message)} characters:")
    print(f"{sum(1 for c in message if c.isupper())} upper letters")
    print(f"{sum(1 for c in message if c.islower())} lower letters")
    print(f"{sum(1 for c in message if c in punctuation)} punctuation marks")
    print(f"{sum(1 for c in message if c in spaces)} spaces")
    print(f"{sum(1 for c in message if c.isdigit())} digits")


if __name__ == "__main__":
    main()
