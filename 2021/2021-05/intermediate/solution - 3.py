import json
from typing import Any


def json_encode(input_data: Any) -> str:
    output = ''
    if type(input_data) == str:
        output = f'"{input_data}"'
    if type(input_data) in [int, float, bool]:
        output = str(input_data).lower()
    if input_data is None:
        output += 'null'
    if type(input_data) in [list, tuple]:
        output += '['
        for _, element in enumerate(input_data):
            output += f'{json_encode(element)}, '
        output = output[:-2]
        output += ']'
    if type(input_data) == dict:
        output += '{'
        for key, value in input_data.items():
            output += f'"{repr(key)}": {json_encode(value)}, '
        output = output[:-2]
        output += '}'
    return output


if __name__ == '__main__':
    object_to_translate = ['a', 1, 2, True, [5, 6], {
        'test': 1,
        'test2': [8, 9],
        3: {
            'a': 'b',
            'c': 'd'
        },
        77: [{'x': 0}, {'y': None}]
    }]
    #object_to_translate = {1:"something","1":"something else"}
    #object_to_translate = {"1":"something",1:"something else"}
    result = json_encode(object_to_translate)
    print(result)
    dump = json.dumps(object_to_translate)
    print(result == dump)
    test = json.loads(result)
    ## Correcting the dictionary
    if type(test) == dict:
        new_test = {}
        for key, value in test.items():
            if "'" in key:
                new_key = key.replace("'","")
            else:
                new_key = int(key)
            new_test[new_key]=test[key]
        test = new_test
    elif type(test) == list:
        for i,test_element in enumerate(test):
             if type(test_element) == dict:   
                 new_test = {}
                 for key, value in test_element.items():
                     if "'" in key:
                         new_key = key.replace("'","")
                     else:
                         new_key = int(key)
                     new_test[new_key]=test_element[key]
                 test[i]=new_test
                