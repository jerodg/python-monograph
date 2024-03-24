#!/usr/bin/env python3
"""Python Monograph: Find the Sum of an Array Between Indexes L and R Using Prefix Sum Solution 00

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


class Solution_00:
    """
    This class provides methods to calculate the sum of elements in an array between two indexes and to check if the array
    contains a target sum.

    Attributes:
        prefix_sum (list[int]): A list that stores the prefix sum of the array.

    Methods:
        get_sum(start: int, end: int) -> int: Returns the sum of array from the start to the end indexes.
        contains_sum(target_sum: int) -> bool: Returns True if array contains the target_sum, False otherwise.
    """

    def __init__(self, array: list[int]) -> None:
        """
        Constructs all the necessary attributes for the Solution_00 object.

        Args:
            array (list[int]): The input array.

        """
        len_array = len(array)
        self.prefix_sum = [0] * len_array

        # If the array is not empty, initialize the first element of prefix_sum
        if len_array > 0:
            self.prefix_sum[0] = array[0]

        # Calculate the prefix sum of the array
        for i in range(1, len_array):
            self.prefix_sum[i] = self.prefix_sum[i - 1] + array[i]

    def get_sum(self, start: int, end: int) -> int:
        """
        Returns the sum of array from the start to the end indexes.

        Args:
            start (int): The start index.
            end (int): The end index.

        Returns:
            int: The sum of array from the start to the end indexes.

        Raises:
            IndexError: If the end index is out of range.

        Examples:
            >>> Solution_00([1, 2, 3]).get_sum(0, 2)
            6
            >>> Solution_00([1, 2, 3]).get_sum(1, 2)
            5
            >>> Solution_00([1, 2, 3]).get_sum(2, 2)
            3
            >>> Solution_00([1, 2, 3]).get_sum(2, 3)
            Traceback (most recent call last):
            ...
            IndexError: list index out of range
        """
        if start == 0:
            return self.prefix_sum[end]

        return self.prefix_sum[end] - self.prefix_sum[start - 1]

    def contains_sum(self, target_sum: int) -> bool:
        """
        Returns True if array contains the target_sum, False otherwise.

        Args:
            target_sum (int): The target sum.

        Returns:
            bool: True if array contains the target_sum, False otherwise.

        Examples:
            >>> Solution_00([1, 2, 3]).contains_sum(6)
            True
            >>> Solution_00([1, 2, 3]).contains_sum(5)
            True
            >>> Solution_00([1, 2, 3]).contains_sum(3)
            True
            >>> Solution_00([1, 2, 3]).contains_sum(4)
            False
            >>> Solution_00([1, 2, 3]).contains_sum(7)
            False
            >>> Solution_00([1, -2, 3]).contains_sum(2)
            True
        """

        # Initialize a set to store the sums
        sums = {0}
        for sum_item in self.prefix_sum:
            # If the difference between the current sum and the target sum is in the set, return True
            if sum_item - target_sum in sums:
                return True

            # Add the current sum to the set
            sums.add(sum_item)

        # If no matching sum is found, return False
        return False


if __name__ == '__main__':
    print(__doc__)
