"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters  -> Solution 01

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
import re


def split_string_into_groups(string: str, n: int) -> list:
    """
    Splits a given string into groups of `n` consecutive characters.

    This function uses Python's `re` (regex) module to solve the problem.
    It uses the `re.findall()` function with a regular expression that matches any `n` characters
    to split the string into groups of `n` characters.

    Args:
        string (str): The input string to be split.
        n (int): The size of the groups in which the string should be split.

    Returns:
        list: A list of strings, where each string in the list is a group of `n` consecutive characters
        from the input string. The groups are formed from left to right. If the length of the string
        is not a multiple of `n`, the last group may contain less than `n` characters.

    Raises:
        ValueError: If the group size `n` is not a positive integer.

    Examples:
        >>> split_string_into_groups("HelloWorld", 3)
        ['Hel', 'loW', 'orl', 'd']

        >>> split_string_into_groups("Python", 2)
        ['Py', 'th', 'on']

        >>> split_string_into_groups("abcdef", 0)
        Traceback (most recent call last):
        ...
        ValueError: The group size must be a positive integer
    """
    # Check if the group size is a positive integer
    if n <= 0:
        raise ValueError("The group size must be a positive integer")

    # Use regex to split the string into groups of `n` characters
    return re.findall('.{1,' + str(n) + '}', string)
