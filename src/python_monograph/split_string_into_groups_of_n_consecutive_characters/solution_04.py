"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters  -> Solution 04

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
from typing import Generator


def split_string_into_groups(string: str, n: int) -> Generator[str, None, None]:
    """
    Generator function to split a string into groups of `n` consecutive characters.

    Args:
        string (str): The input string to be split.
        n (int): The size of the groups.

    Yields:
        str: The next group of `n` characters.

    Raises:
        ValueError: If `n` is not a positive integer.

    Examples:
        >>> list(split_string_into_groups("HelloWorld", 3))
        ['Hel', 'loW', 'orl', 'd']
        >>> list(split_string_into_groups("Python", 2))
        ['Py', 'th', 'on']
        >>> list(split_string_into_groups("1234567890", 4))
        ['1234', '5678', '90']
        >>> list(split_string_into_groups("abc", 1))
        ['a', 'b', 'c']
        >>> list(split_string_into_groups("abc", 5))
        ['abc']
    """
    # Check if `n` is a positive integer.
    if n <= 0:
        raise ValueError("The group size must be a positive integer")

    # Iterate over the string with a step size of `n`.
    for i in range(0, len(string), n):
        # Yield the next group of `n` characters.
        yield string[i:i + n]
