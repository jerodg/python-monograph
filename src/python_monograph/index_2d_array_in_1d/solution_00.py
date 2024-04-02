#!/usr/bin/env python3
"""Python Monograph: Index 2D Array in 1D Solution 00

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
"""
Retrieves the value of an 0-indexed 1D index from a 2D array.
There are two ways to retrieve value(s):

1. Index2DArrayIterator(matrix) -> Iterator[int]
This iterator allows you to iterate through a 2D array by passing in the matrix and
calling next(your_iterator). You can also use the iterator in a loop.
Examples:
list(Index2DArrayIterator(matrix))
set(Index2DArrayIterator(matrix))
tuple(Index2DArrayIterator(matrix))
sum(Index2DArrayIterator(matrix))
-5 in Index2DArrayIterator(matrix)

2. index_2d_array_in_1d(array: list[int], index: int) -> int
This function allows you to provide a 2D array and a 0-indexed 1D integer index,
and retrieves the integer value at that index.

Python doctests can be run using this command:
python3 -m doctest -v index_2d_array_in_1d.py
"""
from collections.abc import Iterator
from dataclasses import dataclass


@dataclass
class Index2DArrayIterator:
    """A class that represents an iterator for a 2D array.

    Attributes:
        matrix (list[list[int]]): A 2D array to iterate over.

    Methods:
        __iter__: Returns an iterator object.
    """

    matrix: list[list[int]]

    def __iter__(self) -> Iterator[int]:
        """The __iter__ method for the Index2DArrayIterator class.

        This method allows the Index2DArrayIterator object to be used in a for loop,
        and other places where an iterator would be expected.

        Yields:
            int: The next value from the 2D array.

        Examples:
            >>> tuple(Index2DArrayIterator([[5], [-523], [-1], [34], [0]]))
            (5, -523, -1, 34, 0)
            >>> tuple(Index2DArrayIterator([[5, -523, -1], [34, 0]]))
            (5, -523, -1, 34, 0)
            >>> tuple(Index2DArrayIterator([[5, -523, -1, 34, 0]]))
            (5, -523, -1, 34, 0)
            >>> t = Index2DArrayIterator([[5, 2, 25], [23, 14, 5], [324, -1, 0]])
            >>> tuple(t)
            (5, 2, 25, 23, 14, 5, 324, -1, 0)
            >>> list(t)
            [5, 2, 25, 23, 14, 5, 324, -1, 0]
            >>> sorted(t)
            [-1, 0, 2, 5, 5, 14, 23, 25, 324]
            >>> tuple(t)[3]
            23
            >>> sum(t)
            397
            >>> -1 in t
            True
            >>> t = iter(Index2DArrayIterator([[5], [-523], [-1], [34], [0]]))
            >>> next(t)
            5
            >>> next(t)
            -523
        """
        for row in self.matrix:
            yield from row


def index_2d_array_in_1d(array: list[list[int]], index: int) -> int:
    """Retrieves the value of the one-dimensional index from a two-dimensional array.

    This function takes a 2D array and a 1D index as input and returns the value at the 1D index in the 2D array.
    The 2D array is assumed to be a list of lists of integers where all rows are the same size and all columns are the same size.
    The 1D index is assumed to be a non-negative integer.

    Args:
        array (list[list[int]]): A 2D array of integers where all rows are the same size and all columns are the same size.
        index (int): A 1D index.

    Returns:
        int: The 0-indexed value of the 1D index in the array.

    Raises:
        ValueError: If there are no items in the array or if the index is out of range.

    Examples:
        >>> index_2d_array_in_1d([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], 5)
        5
        >>> index_2d_array_in_1d([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], -1)
        Traceback (most recent call last):
            ...
        ValueError: index out of range
        >>> index_2d_array_in_1d([[0, 1, 2, 3], [4, 5, 6, 7], [8, 9, 10, 11]], 12)
        Traceback (most recent call last):
            ...
        ValueError: index out of range
        >>> index_2d_array_in_1d([[]], 0)
        Traceback (most recent call last):
            ...
        ValueError: no items in array
    """
    rows = len(array)
    cols = len(array[0])

    # Check if the array is empty
    if rows == 0 or cols == 0:
        raise ValueError('no items in array')

    # Check if the index is out of range
    if index < 0 or index >= rows * cols:
        raise ValueError('index out of range')

    # Return the value at the 1D index in the 2D array
    return array[index // cols][index % cols]


if __name__ == '__main__':
    print(__doc__)
