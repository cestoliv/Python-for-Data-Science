def all_thing_is_obj(object: any) -> int:
    if type(object) == list:
        print('List :', type(object))
    elif type(object) == tuple:
        print('Tuple :', type(object))
    elif type(object) == set:
        print('Set :', type(object))
    elif type(object) == dict:
        print('Dict :', type(object))
    elif type(object) == str:
        print(object, ':', type(object))
    else:
        print('Type not found')
    print(isinstance(object, object))
    return 42
