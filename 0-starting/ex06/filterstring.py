import sys
from ft_filter import ft_filter


def main():
    """
        Take a sys.argv input and output each word of sys.argv[1] that contains
        more characters then sys.argv[2]
    """
    if len(sys.argv) > 3:
        print("AssertionError: more than two argument are provided")
        exit(0)
    elif len(sys.argv) < 3:
        print("AssertionError: less than two argument are provided")
        exit(0)

    if not sys.argv[2].isdigit():
        print("AssertionError: argument is not an integer")
        exit(0)

    words = sys.argv[1].split(' ')
    size = int(sys.argv[2])
    print(list(ft_filter(lambda x: len(x) > size, words)))


if __name__ == "__main__":
    main()
