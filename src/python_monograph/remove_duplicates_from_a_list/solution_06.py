#!/usr/bin/env python3
"""Python Monograph: Remove Duplicates from a Sorted Array Solution 06

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


def solution_06(ls: list) -> list:
    """
    This function removes duplicates from a list in Python using the dict.fromkeys() method.

    Args:
        ls (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed.

    Note:
        This function uses the dict.fromkeys() method to remove duplicates. The dict.fromkeys() method creates a new
        dictionary with the elements of the list as keys and None as their values. Since a dictionary cannot have duplicate
        keys, this method effectively removes duplicates from the list. The function then converts the keys of the dictionary
        back to a list.

    Example:
        >>> solution_06([1, 2, 2, 3, 4, 4, 5, 6, 6])
        [1, 2, 3, 4, 5, 6]

    """
    # Use dict.fromkeys() to remove duplicates and convert the keys back to a list
    return list(dict.fromkeys(ls))


if __name__ == '__main__':
    print(__doc__)
