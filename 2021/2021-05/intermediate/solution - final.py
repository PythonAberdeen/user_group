import json
from typing import Any


def json_decode(input_data: Any) -> str:
    output = ''
    if type(input_data) == str:
        output = f'"{input_data}"'
    if type(input_data) in [int, float, bool]:
        output = str(input_data).lower()
    if input_data is None:
        output += 'null'
    if type(input_data) in [list, tuple]:
        output += '[{}]'.format(', '.join(
            [json_decode(value) for _, value in enumerate(input_data)]))
    if type(input_data) == dict:
        output += '{{{}}}'.format(", ".join(
            [f'"{repr(key)}": {json_decode(value)}'
             for key, value in input_data.items()]))
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
    result = json_decode(object_to_translate)
    print(result)
    dump = json.dumps(object_to_translate)
    print(result == dump)
    test = json.loads(result)
