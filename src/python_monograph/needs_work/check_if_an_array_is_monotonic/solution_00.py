#!/usr/bin/env python3
"""Python Monograph: Check if an Array is Monotonic Solution 00

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


def solution_00(nums: list[int]) -> bool:
    """Check if a list is monotonic using a generator expression and the built-in `all()` function otherwise known as the
    two-pass method.

    This function checks if a given list of integers is monotonic. A list is considered monotonic if it is either entirely
    non-increasing or non-decreasing.

    Args:
        nums (list[int]): The list of integers to check.

    Returns:
        bool: True if the list is monotonic, False otherwise.

    Examples:
        >>> solution_00([1, 2, 2, 3])
        True
        >>> solution_00([6, 5, 4, 4])
        True
        >>> solution_00([1, 3, 2])
        False
    """
    return all(nums[i] <= nums[i + 1] for i in range(len(nums) - 1)) or all(
        nums[i] >= nums[i + 1] for i in range(len(nums) - 1))


if __name__ == '__main__':
    print(__doc__)
