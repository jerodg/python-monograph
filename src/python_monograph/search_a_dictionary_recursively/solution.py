#!/usr/bin/env python3
"""Python Monograph: Search a Dictionary Recursively

Copyright ©2024 Jerod Gawne <https://github.com/jerodg/>

This program is free software: you can redistribute it and/or modify
it under the terms of the Server Side Public License (SSPL) as
published by MongoDB, Inc., either version 1 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
SSPL for more details.

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
You should have received a copy of the SSPL along with this program.
If not, see <https://www.mongodb.com/licensing/server-side-public-license>."""


def method_0(dictionary, target_key):
    """This function searches for a target key in a dictionary recursively.
    If the key is in the dictionary, it returns the value.
    If the key is not in the dictionary, it iterates over the dictionary's values.
    If a value is a dictionary, it calls itself with the value (the nested dictionary) and the target key as arguments.

    Parameters:
    dictionary (dict): The dictionary to be searched.
    target_key (Any): The key to be searched for in the dictionary.

    Returns:
    Any: The value of the first occurrence of the target key. If the key is not found, it returns None.
    """
    if target_key in dictionary:
        return dictionary[target_key]
    else:
        for key in dictionary:
            if isinstance(dictionary[key], dict):
                result = method_0(dictionary[key], target_key)

                if result is not None:
                    return result

    return None


def method_1(dictionary, target_key) -> Generator[Any]:
    """This function searches for a target key in a dictionary recursively using a generator.
    It iterates over the dictionary's items. If the key matches the target key, it yields the value.
    If the value is a dictionary, it yields from a recursive call to itself with the value (the nested dictionary) and the target
    key as arguments.

    Parameters:
    dictionary (dict): The dictionary to be searched.
    target_key (Any): The key to be searched for in the dictionary.

    Returns:
    Generator[Any, None, None]: A generator that yields the values of all occurrences of the target key. If the key is not found,
    it does not yield anything.
    """
    for key, value in dictionary.items():
        if key == target_key:
            yield value
        elif isinstance(value, dict):
            yield from method_1(value, target_key)


if __name__ == '__main__':
    print(__doc__)
