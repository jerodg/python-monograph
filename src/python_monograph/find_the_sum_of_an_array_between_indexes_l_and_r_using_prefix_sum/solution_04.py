#!/usr/bin/env python3
"""Python Monograph: Find the Sum of an Array Between Indexes L and R Using Prefix Sum Solution 04

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
import math


class Solution_04:
    """
    This class provides methods to build a block array from an input array, update a value at a particular index in the array,
    and calculate the sum of elements in the array between two indexes.

    Attributes:
        n (int): The length of the array.
        block_size (int): The size of each block.
        blocks (list[int]): A list that represents the block array.
        arr (list[int]): The input array.

    Methods:
        preprocess() -> None: Preprocesses the input array and fills the block array.
        update(i: int, val: int) -> None: Updates the value at index i in the array.
        query(l: int, r: int) -> int: Returns the sum of elements in the array from index l to r.
    """

    def __init__(self, arr: list[int]) -> None:
        """
        Constructs all the necessary attributes for the Solution_04 object.

        Args:
            arr (list[int]): The input array.

        Examples:
            >>> st = Solution_04([1, 2, 3, 4, 5])
            >>> st.blocks
            [6, 9]
        """
        if not arr:
            raise ValueError('Array cannot be empty')

        if not all(isinstance(item, int) for item in arr):
            raise TypeError('Array must contain only integers')

        self.n = len(arr)
        self.block_size = int(math.sqrt(self.n)) + 1
        self.blocks = [0] * self.block_size
        self.arr = arr
        self.preprocess()

    def preprocess(self) -> None:
        """
        Preprocesses the input array and fills the block array.

        Examples:
            >>> st = Solution_04([1, 2, 3, 4, 5])
            >>> st.preprocess()
            >>> st.blocks
            [6, 9]
        """
        for i in range(self.n):
            self.blocks[i // self.block_size] += self.arr[i]

    def update(self, i: int, val: int) -> None:
        """
        Updates the value at index i in the array.

        Args:
            i (int): The index to be updated.
            val (int): The new value.

        Examples:
            >>> st = Solution_04([1, 2, 3, 4, 5])
            >>> st.update(1, 10)
            >>> st.blocks
            [15, 9]
        """
        block = i // self.block_size
        self.blocks[block] += val - self.arr[i]
        self.arr[i] = val

    def query(self, l: int, r: int) -> int:
        """
        Returns the sum of elements in the array from index l to r.

        Args:
            l (int): The start index.
            r (int): The end index.

        Returns:
            int: The sum of elements in the array from index l to r.

        Examples:
            >>> st = Solution_04([1, 2, 3, 4, 5])
            >>> st.query(1, 3)
            9
            >>> st.query(2, 4)
            12
        """
        start_block = l // self.block_size
        end_block = r // self.block_size
        sum = 0

        if start_block == end_block:
            for i in range(l, r + 1):
                sum += self.arr[i]
        else:
            for i in range(l, (start_block + 1) * self.block_size):
                sum += self.arr[i]
            for i in range(start_block + 1, end_block):
                sum += self.blocks[i]
            for i in range(end_block * self.block_size, r + 1):
                sum += self.arr[i]

        return sum


if __name__ == '__main__':
    print(__doc__)
