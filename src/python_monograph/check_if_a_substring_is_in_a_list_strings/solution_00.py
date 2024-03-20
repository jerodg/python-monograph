#!/usr/bin/env python3
"""Python Monograph: Check if a Substring is in a List of Strings Solution 00

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


def solution_00(data: List[str], substr: str) -> bool:
    """This function checks if a given substring is present in any of the strings in a list using the any() function.

    Parameters:
        data (List[str]): A list of strings where the substring will be searched.
        substr (str): The substring to search in the list of strings.

    Returns:
        bool: True if the substring is found in any string in the list, False otherwise.

    Note:
        This function does not provide the location of the substring in the string.

    Example:
    >>> solution_00(['apple', 'banana', 'cherry'], 'app')
        True
    >>> solution_00(['apple', 'banana', 'cherry'], 'z')
        False

    References:
        https://docs.python.org/3/library/functions.html?highlight=any#any
    """
    # Check if the substring is None. If it is, raise a TypeError.
    if substr is None:
        raise TypeError('NoneType found in substr')

    # Check if any element in the list is None. If it is, raise a TypeError.
    if None in data:
        raise TypeError('NoneType found in list')

    # Use the any() function to check if the substring is in any string in the list.
    # The any() function returns True if at least one element is True.
    # The 'in' operator checks if the substring is a part of each string.
    # The 'for' loop iterates over each string in the list.
    # If the substring is found in any string, the function returns True. Otherwise, it returns False.
    return any(substr in x for x in data)


if __name__ == '__main__':
    print(__doc__)
