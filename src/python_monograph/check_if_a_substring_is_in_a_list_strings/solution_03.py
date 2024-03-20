#!/usr/bin/env python3
"""Python Monograph: Check if a Substring is in a List of Strings Solution 03

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


def solution_03(data: List[str], substr: str) -> bool:
    """This function checks if a given substring is found in a joined string of a list using the join() method.

    The join() method concatenates all the strings in the list into a single string with a specified delimiter.
    In this case, the delimiter is a tab character ("\t").

    After joining the strings, the function checks if the substring is found in the resulting string.

    Parameters:
        data (List[str]): A list of strings to be joined and where the substring will be searched.
        substr (str): The substring to search in the joined string.

    Returns:
        bool: True if the substring is found in the joined string, False otherwise.

    Example:
    >>> solution_03(['apple', 'banana', 'cherry'], 'app')
        True
    >>> solution_03(['apple', 'banana', 'cherry'], 'z')
        False

    References:
        https://docs.python.org/3/library/stdtypes.html?highlight=join#str.join
    """
    if substr is None:
        raise TypeError('NoneType found in substr')

    if None in data:
        raise TypeError('NoneType found in list')

    try:
        return substr in '\t'.join(data)
    except TypeError:
        raise TypeError('NoneType found in list')


if __name__ == '__main__':
    print(__doc__)
