#!/usr/bin/env python3
"""Python Monograph: Remove Duplicates from a Sorted Array Solution 08

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

import numpy as np


def solution_08(ls: list) -> list:
    """
    This function removes duplicates from a list in Python using the numpy library.

    Args:
        ls (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed.

    Note:
        This function uses the numpy library to remove duplicates. It first converts the list to a numpy array,
        then uses the unique() method to remove duplicates. The tolist() method is then used to convert the numpy array
        back to a list.

    Example:
        >>> solution_08([1, 2, 2, 3, 4, 4, 5, 6, 6])
        [1, 2, 3, 4, 5, 6]
    """
    # Convert the list to a numpy array
    # Use the unique() method to remove duplicates
    # Convert the numpy array back to a list using the tolist() method
    return np.unique(ls).tolist()


if __name__ == '__main__':
    print(__doc__)
