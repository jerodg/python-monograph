#!/usr/bin/env python3
"""Python Monograph: Find the Sum of an Array Between Indexes L and R Using Prefix Sum Solution 03

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
from math import log2


class Solution_03:
    """
    This class provides methods to build a sparse table from an array and query the minimum value in a range.

    Attributes:
        n (int): The length of the array.
        table (list[list[int]]): A 2D list that represents the sparse table.

    Methods:
        build_table(arr: list[int]) -> list[list[int]]: Builds the sparse table from the array.
        query(l: int, r: int) -> int: Returns the minimum value in the array from index l to r.
    """

    def __init__(self, arr: list[int]) -> None:
        """
        Constructs all the necessary attributes for the Solution_03 object.

        Args:
            arr (list[int]): The input array.

        Examples:
            >>> st = Solution_03([1, 2, 3, 4, 5])
            >>> st.table
            [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
        """
        if not arr:
            raise ValueError('Array cannot be empty')

        if not all(isinstance(item, int) for item in arr):
            raise TypeError('Array must contain only integers')

        self.n = len(arr)
        self.table = self.build_table(arr)

    def build_table(self, arr: list[int]) -> list[list[int]]:
        """
        Builds the sparse table from the array.

        Args:
            arr (list[int]): The input array.

        Returns:
            list[list[int]]: The sparse table.

        Examples:
            >>> st = Solution_03([1, 2, 3, 4, 5])
            >>> st.build_table([1, 2, 3, 4, 5])
            [[1, 1, 1], [2, 2, 2], [3, 3, 3], [4, 4, 4], [5, 5, 5]]
        """
        k = int(log2(self.n)) + 1
        table = [[0] * k for _ in range(self.n)]
        for i in range(self.n):
            table[i][0] = arr[i]
        for j in range(1, k):
            i = 0
            while i + (1 << j) <= self.n:
                table[i][j] = min(table[i][j - 1], table[i + (1 << (j - 1))][j - 1])
                i += 1
        return table

    def query(self, l: int, r: int) -> int:
        """
        Returns the minimum value in the array from index l to r.

        Args:
            l (int): The start index.
            r (int): The end index.

        Returns:
            int: The minimum value in the array from index l to r.

        Examples:
            >>> st = Solution_03([1, 2, 3, 4, 5])
            >>> st.query(1, 3)
            2
            >>> st.query(2, 4)
            3
        """
        j = int(log2(r - l + 1))
        return min(self.table[l][j], self.table[r - (1 << j) + 1][j])


if __name__ == '__main__':
    print(__doc__)
