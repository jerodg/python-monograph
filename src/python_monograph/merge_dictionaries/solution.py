#!/usr/bin/env python3
"""Python Monograph: Merge Dictionaries Solutions

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
from collections import ChainMap, defaultdict
from itertools import chain


def method_0(x: dict, y: dict) -> dict:
    """Merge two dictionaries by creating a copy of the first dictionary and updating it with the second one.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    The original dictionaries are not modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    temp = x.copy()
    temp.update(y)
    return temp


def method_1(x: dict, y: dict) -> dict:
    """Merge two dictionaries by adding items from both.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    The original dictionaries are not modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    return dict(list(x.items()) + list(y.items()))


def method_2(x: dict, y: dict) -> dict:
    """Merge two dictionaries using the unpacking operator.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    This method requires Python 3.5 or later.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    return {**x, **y}


def method_3(x: dict, y: dict) -> dict:
    """Merge two dictionaries using ChainMap from collections.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the first dictionary is used.
    The original dictionaries are not modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    return dict(ChainMap({}, y, x))


def method_4(x: dict, y: dict) -> dict:
    """Merge two dictionaries using itertools.chain.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    The original dictionaries are not modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    return dict(chain(x.items(), y.items()))


def method_5(x: dict, y: dict) -> dict:
    """Merge two dictionaries using the union operator.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    This method requires Python 3.9 or later.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    return x | y


def method_6(x: dict, y: dict) -> dict:
    """Merge two dictionaries using a generator expression and the next function.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    The original dictionaries are not modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    return next(z.update(y) or z for z in [x.copy()])


def method_7(x: dict, y: dict) -> dict:
    """Merge two dictionaries using a lambda function and the update method.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    The original dictionaries are not modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    return (lambda z: z.update(y) or z)(x.copy())


def method_8(x: dict, y: dict) -> dict:
    """Merge two dictionaries using dictionary comprehension.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys and values from both
    dictionaries.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    The original dictionaries are not modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys and values from both input dictionaries.
    """
    return {k: v for d in [x, y] for k, v in d.items()}


def method_9(x: dict, y: dict) -> dict:
    """Merge two dictionaries using the update method.

    This function takes two dictionaries as input and updates the first dictionary with the keys and values from the second
    dictionary.
    If a key is present in both dictionaries, the value from the second dictionary is used.
    The original first dictionary is modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        The first dictionary after it has been updated with the keys and values from the second dictionary.
    """
    x.update(y)
    return x


def method_10(x: dict, y: dict) -> dict:
    """Merge two dictionaries using defaultdict from collections.

    This function takes two dictionaries as input and returns a new dictionary that contains all the keys from both dictionaries.
    If a key is present in both dictionaries, the values are stored in a list.
    The original dictionaries are not modified.

    Args:
        x: The first dictionary.
        y: The second dictionary.

    Returns:
        A new dictionary that contains all the keys from both input dictionaries. The values are stored in a list.
    """
    merged = defaultdict(list)
    for d in (x, y):
        for key, value in d.items():
            merged[key].append(value)
    return merged


if __name__ == '__main__':
    print(__doc__)
