#!/usr/bin/env python3
"""Python Monograph: Remove Duplicates from a Sorted Array Solution 00

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


def solution_00(ls: list) -> list:
    """
    This function removes duplicates from a list in Python.

    Args:
        ls (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed.

    Note:
        This function uses the set data structure to remove duplicates. The set data structure in Python
        does not allow duplicates, so when a list is converted to a set, all duplicates are automatically removed.
        However, sets are unordered, so the original order of elements in the list is not preserved.

    Example:
        >>> solution_00([1, 2, 2, 3, 4, 4, 5, 6, 6])
        [1, 2, 3, 4, 5, 6]
    """
    # Convert the list to a set to remove duplicates
    # Then convert the set back to a list
    return list(set(ls))


if __name__ == '__main__':
    print(__doc__)
