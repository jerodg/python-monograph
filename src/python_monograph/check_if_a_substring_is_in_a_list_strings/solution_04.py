#!/usr/bin/env python3
"""Python Monograph: Check if a Substring is in a List of Strings Solution 04

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


def solution_04(data: List[str], substr: str) -> bool:
    """This function checks if a given substring is found in any of the strings in a list using a for-loop.

    The function iterates over each string in the list using a for-loop.
    For each string, it checks if the substring is found in the string using the 'in' operator.
    If the substring is found in any string, the function immediately returns True.
    If the substring is not found in any string after iterating over the entire list, the function returns False.

    Parameters:
        data (List[str]): A list of strings where the substring will be searched.
        substr (str): The substring to search in the list of strings.

    Returns:
        bool: True if the substring is found in any string in the list, False otherwise.

    Raises:
        TypeError: If the substring or any element in the list is None.

    Example:
    >>> solution_04(['apple', 'banana', 'cherry'], 'app')
        True
    >>> solution_04(['apple', 'banana', 'cherry'], 'z')
        False

    References:
        https://docs.python.org/3/tutorial/controlflow.html?highlight=loop#for-statements
    """
    # Check if the substring is None
    if substr is None:
        raise TypeError('NoneType found in substr')

    try:
        # Iterate over each string in the list
        for row in data:
            # Check if the substring is found in the string
            if substr in row:
                # If the substring is found, return True
                return True
    except TypeError:
        # If any element in the list is None, raise a TypeError
        raise TypeError('NoneType found in list')

    # If the substring is not found in any string after iterating over the entire list, return False
    return False


if __name__ == '__main__':
    print(__doc__)
