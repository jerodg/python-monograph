#!/usr/bin/env python3
"""Python Monograph: Find the Sum of an Array Between Indexes L and R Using Prefix Sum Solution 02

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


class Solution_02:
    """
    This class provides methods to build a Fenwick Tree (Binary Indexed Tree) from an array, update a value at a particular index
    in the array,
    and calculate the sum of elements in the array between two indexes.

    Attributes:
        size (int): The size of the array.
        tree (list[int]): A list that represents the Fenwick Tree.

    Methods:
        update(i: int, val: int) -> None: Updates the value at index i in the array.
        query(i: int) -> int: Returns the prefix sum up to index i in the array.
        range_query(l: int, r: int) -> int: Returns the sum of elements in the array from index l to r.
    """

    def __init__(self, size: int) -> None:
        """
        Constructs all the necessary attributes for the Solution_02 object.

        Args:
            size (int): The size of the array.

        """
        if not isinstance(size, int):
            raise TypeError('Size must be an integer')

        if not size > 0:
            raise ValueError('Size must be a positive integer')

        self.size = size
        self.tree = [0] * (size + 1)

    def update(self, i: int, val: int) -> None:
        """
        Updates the value at index i in the array.

        Args:
            i (int): The index to be updated.
            val (int): The new value.

        """
        while i <= self.size:
            self.tree[i] += val
            i += i & -i

    def query(self, i: int) -> int:
        """
        Returns the prefix sum up to index i in the array.

        Args:
            i (int): The index.

        Returns:
            int: The prefix sum up to index i in the array.

        Examples:
            >>> fenwick_tree = Solution_02(5)
            >>> for i in range(1, 6):
            ...     fenwick_tree.update(i, i)
            >>> fenwick_tree.query(3)
            6
            >>> fenwick_tree.query(5)
            15
        """
        res = 0
        while i:
            res += self.tree[i]
            i -= i & -i
        return res

    def range_query(self, l: int, r: int) -> int:
        """
        Returns the sum of elements in the array from index l to r.

        Args:
            l (int): The start index.
            r (int): The end index.

        Returns:
            int: The sum of elements in the array from index l to r.

        Examples:
            >>> fenwick_tree = Solution_02(5)
            >>> for i in range(1, 6):
            ...     fenwick_tree.update(i, i)
            >>> fenwick_tree.range_query(2, 4)
            9
            >>> fenwick_tree.range_query(1, 5)
            15
        """
        return self.query(r) - self.query(l - 1)


if __name__ == '__main__':
    print(__doc__)
