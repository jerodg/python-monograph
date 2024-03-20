#!/usr/bin/env python3
"""Python Monograph: Check if a Substring is in a List of Strings Solution 02

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


def solution_02(data: List[str], substr: str) -> bool:
    """This function checks if a given substring is found in any of the strings in a list using the find() method and a list
    comprehension.

    The find() method returns the lowest (first) index in the string where the substring is found within the slice.
    If the substring is not found, the find() method returns -1.

    A list comprehension is used to iterate over the list of strings and apply the find() method to each string.
    If the substring is found in any string (find() method does not return -1), the list comprehension will return a list with at
    least one element, and the function will return True.
    If the substring is not found in any string, the list comprehension will return an empty list, and the function will return
    False.

    Parameters:
        data (List[str]): A list of strings where the substring will be searched.
        substr (str): The substring to search in the list of strings.

    Returns:
        bool: True if the substring is found in any string in the list, False otherwise.

    Raises:
        AttributeError: If any element in the list is None.

    Example:
    >>> solution_02(['apple', 'banana', 'cherry'], 'app')
        True
    >>> solution_02(['apple', 'banana', 'cherry'], 'z')
        False

    References:
        https://docs.python.org/3/library/stdtypes.html?highlight=find#str.find
    """
    # Check if any element in the list is None. If it is, raise an AttributeError.
    if None in data:
        raise AttributeError('NoneType found in list')

    # Use a list comprehension to iterate over the list of strings and apply the find() method to each string.
    # If the substring is found in any string (find() method does not return -1), the list comprehension will return a list with at
    # least one element, and the function will return True.
    # If the substring is not found in any string, the list comprehension will return an empty list, and the function will return
    # False.
    return True if [x for x in data if x.find(substr) != -1] else False


if __name__ == '__main__':
    print(__doc__)
