"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters  -> Solution 05

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
from itertools import islice
from typing import Iterator


def split_string_into_groups(s: str, n: int) -> Iterator[str]:
    """
    Splits a string into groups of `n` consecutive characters using itertools.islice().

    Args:
        s (str): The input string to be split.
        n (int): The size of the groups.

    Returns:
        Iterator[str]: An iterator that yields each group of `n` consecutive characters from the input string.

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

    # Create an iterator from the string.
    it = iter(s)

    # Use itertools.islice() to yield groups of `n` characters from the iterator.
    while True:
        group = ''.join(islice(it, n))

        if not group:
            break

        yield group
