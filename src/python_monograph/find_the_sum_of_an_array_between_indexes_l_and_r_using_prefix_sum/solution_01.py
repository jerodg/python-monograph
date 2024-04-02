#!/usr/bin/env python3
"""Python Monograph: Find the Sum of an Array Between Indexes L and R Using Prefix Sum Solution 01

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


class Solution_01:
    """
    This class provides methods to build a segment tree from an array, update a value at a particular index in the array,
    and calculate the sum of elements in the array between two indexes.

    Attributes:
        n (int): The length of the array.
        tree (list[int]): A list that represents the segment tree.

    Methods:
        build_tree(arr: list[int]) -> None: Builds the segment tree from the array.
        update(p: int, value: int) -> None: Updates the value at index p in the array.
        query(l: int, r: int) -> int: Returns the sum of elements in the array from index l to r.
    """

    def __init__(self, arr: list[int]) -> None:
        """
        Constructs all the necessary attributes for the Solution_01 object.

        Args:
            arr (list[int]): The input array.

        Examples:
            >>> st = Solution_01([1, 2, 3, 4, 5])
            >>> st.tree
            [0, 0, 0, 0, 0, 1, 2, 3, 4, 5]
        """
        if not arr:
            raise ValueError('Array cannot be empty')

        if not all(isinstance(item, int) for item in arr):
            raise TypeError('Array must contain only integers')

        self.n = len(arr)
        self.tree = [0] * (2 * self.n)
        self.build_tree(arr)

    def build_tree(self, arr: list[int]) -> None:
        """
        Builds the segment tree from the array.

        Args:
            arr (list[int]): The input array.

        Examples:
            >>> st = Solution_01([1, 2, 3, 4, 5])
            >>> st.build_tree([1, 2, 3, 4, 5])
            >>> st.tree
            [0, 15, 6, 9, 3, 3, 4, 5, 1, 2]
        """
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]

        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i << 1] + self.tree[i << 1 | 1]

    def update(self, p: int, value: int) -> None:
        """
        Updates the value at index p in the array.

        Args:
            p (int): The index to be updated.
            value (int): The new value.

        Examples:
            >>> st = Solution_01([1, 2, 3, 4, 5])
            >>> st.update(1, 10)
            >>> st.tree
            [0, 24, 15, 9, 11, 3, 4, 5, 10, 2]
        """
        p += self.n
        self.tree[p] = value

        while p > 1:
            self.tree[p >> 1] = self.tree[p] + self.tree[p ^ 1]
            p >>= 1

    def query(self, l: int, r: int) -> int:
        """
        Returns the sum of elements in the array from index l to r.

        Args:
            l (int): The start index.
            r (int): The end index.

        Returns:
            int: The sum of elements in the array from index l to r.

        Examples:
            >>> st = Solution_01([1, 2, 3, 4, 5])
            >>> st.query(1, 3)
            6
            >>> st.query(2, 4)
            9
        """
        l += self.n
        r += self.n
        res = 0

        while l < r:
            if l & 1:
                res += self.tree[l]
                l += 1

            if r & 1:
                r -= 1
                res += self.tree[r]

            l >>= 1
            r >>= 1

        return res


if __name__ == '__main__':
    print(__doc__)
