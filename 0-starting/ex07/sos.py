import sys


NESTED_MORSE = {
    " ": "/",
    "A": ".-",
    "B": "-...",
    "C": "-.-.",
    "D": "-..",
    "E": ".",
    "F": "..-.",
    "G": "--.",
    "H": "....",
    "I": "..",
    "J": ".---",
    "K": "-.-",
    "L": ".-..",
    "M": "--",
    "N": "-.",
    "O": "---",
    "P": ".--.",
    "Q": "--.-",
    "R": ".-.",
    "S": "...",
    "T": "-",
    "U": "..-",
    "V": "...-",
    "W": ".--",
    "X": "-..-",
    "Y": "-.--",
    "Z": "--..",
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
}


def main():
    """
        Take a sys.argv input and output sys.argv[1] as morse
    """
    if len(sys.argv) > 2:
        print("AssertionError: more than two argument are provided")
        exit(0)
    elif len(sys.argv) < 2:
        print("AssertionError: less than two argument are provided")
        exit(0)

    for letter in sys.argv[1]:
        if letter.upper() not in NESTED_MORSE:
            print("AssertionError: the arguments are bad")
            exit(0)

    print(' '.join([NESTED_MORSE[letter.upper()] for letter in sys.argv[1]]))


if __name__ == "__main__":
    main()
