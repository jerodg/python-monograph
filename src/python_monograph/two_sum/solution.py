#!/usr/bin/env python3
"""Python Monograph: Two Sum Solutions

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


def method_0(nums: list[int], target: int) -> list[int]:
    """Method 0: Brute Force (iteration)

    This function takes a list of integers and a target integer as input.
    It iterates over the list of integers twice (nested iteration) to find two numbers that add up to the target.
    The function returns a list containing the indices of the two numbers in the original list.
    If no such pair of numbers is found, the function returns None.

    Args:
        nums: A list of integers.
        target: An integer that we want to find two numbers in the list that add up to.

    Returns:
        A list of two integers representing the indices in the original list of the two numbers that add up to the target.
        If no such pair of numbers is found, the function returns None.
    """
    for i, n in enumerate(nums):
        for j, m in enumerate(nums[i + 1 :]):
            if n + m == target:
                return [i, j + i + 1]


def method_1(nums: list[int], target: int) -> list[int]:
    """Method 1: Two-pass Hash Table

    This function takes a list of integers and a target integer as input.
    It uses a hash table (dictionary in Python) to store the integers from the list as keys and their indices as values.
    The function then iterates over the list of integers again, checking if the difference between the target and the current
    integer is in the hash table.
    If it is, and the index of the current integer is not the same as the index stored in the hash table for the difference,
    the function returns a list containing the indices of the two numbers.
    If no such pair of numbers is found, the function returns None.

    Args:
        nums: A list of integers.
        target: An integer that we want to find two numbers in the list that add up to.

    Returns:
        A list of two integers representing the indices in the original list of the two numbers that add up to the target.
        If no such pair of numbers is found, the function returns None.
    """
    d = {}
    for i, n in enumerate(nums):
        d[n] = i

    for i, n in enumerate(nums):
        if target - n in d and i != d[target - n]:
            return [i, d[target - n]]


def method_2(nums: list[int], target: int) -> list[int]:
    """Method 2: One-pass Hash Table

    This function takes a list of integers and a target integer as input.
    It uses a hash table (dictionary in Python) to store the integers from the list as keys and their indices as values.
    The function iterates over the list of integers, checking if the difference between the target and the current integer is in
    the hash table.
    If it is, the function returns a list containing the indices of the two numbers.
    If no such pair of numbers is found, the function returns None.

    Args:
        nums: A list of integers.
        target: An integer that we want to find two numbers in the list that add up to.

    Returns:
        A list of two integers representing the indices in the original list of the two numbers that add up to the target.
        If no such pair of numbers is found, the function returns None.
    """
    d = {}
    for i, n in enumerate(nums):
        if target - n in d:
            return [d[target - n], i]
        d[n] = i


if __name__ == '__main__':
    print(__doc__)
