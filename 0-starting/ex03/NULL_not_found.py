import math


def NULL_not_found(object: any) -> int:
    if object is None:
        print('Nothing:', object, type(object))
    elif type(object) == float and math.isnan(object):
        print('Cheese:', object, type(object))
    elif type(object) == int and object == 0:
        print('Zero:', object, type(object))
    elif type(object) == str and not object:
        print('Empty:', type(object))
    elif type(object) == bool and not object:
        print('Fake:', object, type(object))
    else:
        print('Type not Found')
        return 1
    return 0
