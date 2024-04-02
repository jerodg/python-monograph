#!/usr/bin/env python3
"""Python Monograph: Remove Duplicates from a Sorted Array Solution 05

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


def solution_05(ls: list) -> list:
    """
    This function removes duplicates from a list in Python using list comprehension and enumerate.

    Args:
        ls (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed.

    Note:
        This function uses list comprehension and the enumerate function to remove duplicates. The enumerate function
        is used to get both the index and the value from the list. The value is then checked if it's in the list after
        the current index. If it's not, it's added to the new list. This way, only the last occurrence of each element
        is kept in the list.

    Example:
        >>> solution_05([1, 2, 2, 3, 4, 4, 5, 6, 6])
        [1, 2, 3, 4, 5, 6]
    """
    # Use list comprehension and enumerate to remove duplicates
    # Only the last occurrence of each element is kept in the list
    return [a for i, a in enumerate(ls) if a not in ls[i + 1:]]


if __name__ == '__main__':
    print(__doc__)
