#!/usr/bin/env python3
"""Python Monograph: Remove Duplicates from a Sorted Array Solution 09

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
import itertools
import operator


def solution_09(ls: list) -> list:
    """
    This function removes duplicates from a sorted list in Python using the itertools.groupby() method.

    Args:
        ls (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed.

    Note:
        This function uses the itertools.groupby() method to remove duplicates. The groupby() method groups consecutive
        elements in the list that are the same. The function then uses a list comprehension to iterate over the groups and
        select the first element from each group (which is done using the next() function). This way, only the first occurrence
        of each element is kept in the list.

    Example:
        >>> solution_09([1, 2, 2, 3, 4, 4, 5, 6, 6])
        [1, 2, 3, 4, 5, 6]
    """
    # Use itertools.groupby() to group consecutive elements that are the same
    # Use a list comprehension to select the first element from each group
    return [next(g) for _, g in itertools.groupby(sorted(ls, key=operator.itemgetter(0))) if g]


if __name__ == '__main__':
    print(__doc__)
