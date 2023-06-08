import numpy as np
import statistics

def roundup(num):
    return int(-(-num // 1))

def mean(array):
    return sum(array) / len(array)

def find_median(array):
    sort = sorted(array)
    middle = (len(sort) - 1) // 2
    if len(sort) % 2 == 0:
        return mean([sort[middle], sort[middle + 1]]), [middle, middle + 1]
    else:
        return sort[middle], [middle]

def median(array) -> float:
    sort = sorted(array)
    middle = (len(sort) - 1) // 2
    if len(sort) % 2 == 0:
        return float(mean([sort[middle], sort[middle + 1]]))
    else:
        return float(sort[middle])
    
def quartile(array):
    sort = sorted(array)
    m, mi = find_median(array)
    q1, q1i = find_median(array[:mi[0]])
    q3, q3i = find_median(array[mi[-1] + 1:])
    # print(q1, q3)
    print(sort[q1i[0]], sort[q1i[-1]], q1i, sort[q3i[0]], sort[q3i[-1]], q3i)
    # q1 = sort[int(25 / 100 * len(sort))]
    # q1 = sort[(len(sort) + 1) // 3 - 1]
    q2i = (len(sort) + 1) // 2
    q1i = q2i // 2
    q3i = q2i + q1i
    # q3 = sort[int(75 / 100 * len(sort))]
    print(np.percentile(array, [25, 75]))
    # return [q1, q3]
    return [sort[q1i - 1], sort[q3i - 1]]

def sqrt(num):
    return num ** 0.5

def standard_deviation(array):
    m = mean(array)
    return sqrt(sum([(x - m) ** 2 for x in array]) / len(array))

def variance(array):
    m = mean(array)
    return 1/len(array) * sum([(x - m) ** 2 for x in array])

def ft_statistics(*args, **kwargs) -> None:
    for a in args:
        if not isinstance(a, (int, float)):
            print('ERROR')
            return
    array = list(args)

    authorized = ['mean', 'median', 'quartile', 'std', 'var']
    for key, value in kwargs.items():
        # print(key)
        if value not in authorized:
            continue
        if len(array) == 0:
            print('ERROR')
            continue

        if value == 'mean':
            print(f'mean : {mean(array)}')
        elif value == 'median':
            print(f'median : {median(array)}')
        elif value == 'quartile':
            print(f'quartile : {quartile(array)}')
        elif value == 'std':
            print(f'std : {standard_deviation(array)}')
        elif value == 'var':
            print(f'var : {variance(array)}')