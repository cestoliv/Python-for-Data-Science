def roundup(num):
    return int(-(-num // 1))


def mean(array):
    return sum(array) / len(array)


def nearest(array, value):
    # value = round(value)
    near = array[0]
    near_r = -1

    for x in array:
        r = abs(x - value)
        if near_r == -1 or (r < near_r or (r == near_r and near >= x)):
            near = x
            near_r = r
    return near


def median(array) -> float:
    sort = sorted(array)
    middle = (len(sort) - 1) // 2
    if len(sort) % 2 == 0:
        return float(mean([sort[middle], sort[middle + 1]]))
    else:
        return float(sort[middle])


def quartile(array):
    sort = sorted(array)

    middle = int(len(sort)//2)
    # if len(sort) % 2 %
    q1 = median(sort[:middle])
    q3 = median(sort[middle:])
    # print(q1, q3)
    return [nearest(sort, q1), nearest(sort, q3)]


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
