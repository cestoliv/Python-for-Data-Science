def roundup(num):
    return int(-(-num // 1))


def mean(array):
    return sum(array) / len(array)


def median(array) -> float:
    sort = sorted(array)
    middle = (len(sort) - 1) // 2
    if len(sort) % 2 == 0:
        return float(mean([sort[middle], sort[middle + 1]]))
    else:
        return float(sort[middle])


# def percentile(array, percent):
#     sort = sorted(array)
#     qi = (len(sort) + 1) * percent
#     qi_ceil = roundup(qi)
#     qi_floor = qi_ceil - 1

#     if qi_ceil == qi_floor:
#         q = sort[qi_floor]
#     else:
#         q = sort[qi_floor] + 0.25 * (sort[qi_ceil] - sort[qi_floor])
#     return q


def quartile(array):
    sort = sorted(array)
    q1i = int(round(25/100 * len(sort) + 0.5))
    q1 = sort[q1i-1]
    q3i = int(round(75/100 * len(sort) + 0.5))
    q3 = sort[q3i-1]

    return [q1, q3]


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
