#!/usr/bin/env python3
"""Python Monograph: Find the Longest Substring Without Repeating Characters Solution 02

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


def solution_02(s: str) -> Tuple[int, str]:
    """This function finds the longest substring without repeating characters in a given string using a sliding window.
    It returns a tuple containing the length of the longest substring and the substring itself.

    Args:
        s (str): The input string.

    Returns:
        Tuple[int, str]: A tuple containing the length of the longest substring and the substring itself.

    Examples:
        >>> solution_02('abcabcbb')
        (3, 'abc')
        >>> solution_02('bbbbbb')
        (1, 'b')
        >>> solution_02('pwwkew')
        (3, 'wke')
    """
    start = max_length = 0
    seen = dict()
    max_str = ''

    for i, c in enumerate(s):
        if seen.get(c, -1) >= start:
            start = seen[c] + 1

        if max_length < i - start + 1:
            max_length = i - start + 1
            max_str = s[start: i + 1]

        seen[c] = i

    return max_length, max_str


if __name__ == '__main__':
    print(__doc__)
