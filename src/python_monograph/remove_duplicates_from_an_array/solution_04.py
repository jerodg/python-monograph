"""
Python Monograph -> Remove Duplicates from an Array -> Solution 04

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
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""
import itertools


def remove_duplicates(arr: list) -> list:
    """
    This function removes duplicates from a given list using the itertools.groupby() function approach.

    Args:
        arr (list): The input list from which duplicates need to be removed.

    Returns:
        list: A new list with duplicates removed. The order of elements is not preserved.

    Doctest:
        >>> remove_duplicates([1, 2, 2, 3, 4, 4, 5, 5])
        [1, 2, 3, 4, 5]
        >>> remove_duplicates(['a', 'b', 'b', 'c', 'd', 'd', 'e', 'e'])
        ['a', 'b', 'c', 'd', 'e']

    Note:
        This function does not preserve the original order of elements in the list.
    """
    if not isinstance(arr, list) or len(arr) == 0:
        raise TypeError('Input list is empty or nonexistent.')

    arr.sort()
    return [key for key, group in itertools.groupby(arr)]
