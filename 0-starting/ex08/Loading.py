import os
import math


def ft_tqdm(lst: range) -> None:
    """
        Decorate an iterable object, returning an iterator which acts exactly
        like the original iterable, but prints a dynamically updating
        progressbar every time a value is requested.
    """
    lenght = len(list(lst))

    size = os.get_terminal_size().columns
    size -= 5  # before progress bar
    size -= len(str(lenght)) * 2 + 3  # after progress bar
    # size -= 26 # not implemented speed

    def print_line(percent, num_colored, num_empty, p):
        print('\r', end='')
        print(f'{percent:3}%|{"█" * num_colored}{" " * num_empty}| ', end='')
        print("{i:{lenght}}".format(i=p, lenght=len(str(lenght))), end='')
        print(f'/{lenght}', end='', flush=True)

    for i in lst:
        if i % 20 == 0:
            percent = int(i / lenght * 100)
            num_colored = math.ceil(size * percent / 100)
            num_empty = size - num_colored
            print_line(percent, num_colored, num_empty, i)
        yield i
    print_line(100, size, 0, lenght)
