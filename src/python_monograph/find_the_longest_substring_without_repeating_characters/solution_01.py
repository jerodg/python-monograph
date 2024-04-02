#!/usr/bin/env python3
"""Python Monograph: Find the Longest Substring Without Repeating Characters Solution 01

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
from collections import deque


def solution_01(s: str) -> tuple[int, str]:
    """Finds the longest substring without repeating characters in a given string using deque.

    This function uses a deque as a sliding window to find the longest substring without repeating characters.
    It iterates over the string, and for each character, it removes elements from the left of the deque until the deque does not
    contain the current character.
    Then it appends the current character to the deque. The maximum length of the deque during this process is the length of the
    longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        tuple[int, str]: A tuple containing the length of the longest substring without repeating characters and the substring
        itself.

    Examples:
        >>> solution_01('abcabcbb')
        (3, 'abc')

        >>> solution_01('bbbbbb')
        (1, 'b')

        >>> solution_01('pwwkew')
        (3, 'wke')
    """
    queue = deque()
    max_length = 0

    for char in s:
        while char in queue:
            queue.popleft()
        queue.append(char)
        max_length = max(max_length, len(queue))

    return max_length, ''.join(list(queue))


if __name__ == '__main__':
    print(__doc__)
