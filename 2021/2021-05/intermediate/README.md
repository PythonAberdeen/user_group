# Intermediate Challenge May 2021

Write a `json_encode()` function to return a [JSON](https://www.json.org/json-en.html) string for the python data structure passed to it. 

Encode with the following mappings:
| Python      | JSON   |
|-------------|--------|
| None        | null   |
| False       | false  |
| True        | true   |
| int, float  | number |
| str         | string |
| list, tuple | array  |
| dict        | object |

There are some differences between the python and JSON data structures that you will have to decide how to deal with. For example, a python `dict` can have keys of any hashable type but JSON `object` keys are always strings. `{1: "something", "1": "something else"}` is a perfectly acceptable python `dict`, but if encoded to a JSON `object` by converting the keys to `str` would have two identical keys. 

You can test the output of your `json_encode()` by running it through `json.loads()` to see that you get back something that matches the original data structure (except where there isn't a one-to-one mapping between python and JSON). 

Can you add support for other python data structures? Sets? Dataclasses? Objects?

Compare your `json_encode()` function to [the encoder](https://github.com/python/cpython/blob/main/Lib/json/encoder.py) from the `json` module of the python standard library. 
