#!/usr/bin/env python3
"""Python Monograph: Remove Duplicates from a Sorted Array Solution 04

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


def solution_04(ls: list) -> list:
    """
    This function removes duplicates from a list in Python using a for loop and a conditional statement.

    Args:
        ls (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed.

    Note:
        This function uses a for loop to iterate over the input list. For each element in the list, it checks if the
        element is already in the unique list. If it's not, it appends the element to the unique list. This way, only
        the first occurrence of each element is kept in the list.

    Example:
        >>> solution_04([1, 2, 2, 3, 4, 4, 5, 6, 6])
        [1, 2, 3, 4, 5, 6]
    """
    # Initialize an empty list to store unique elements
    unique = []
    # Use a for loop to iterate over the input list
    for item in ls:
        # If the current item is not in the unique list, append it
        if item not in unique:
            unique.append(item)
    # Return the list of unique elements
    return unique


if __name__ == '__main__':
    print(__doc__)
