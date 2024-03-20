#!/usr/bin/env python3
"""Python Monograph: Find the Longest Substring Without Repeating Characters Solution 00

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


def solution_00(s: str) -> tuple[int, str]:
    """Finds the longest substring without repeating characters in a given string using the sliding window technique.

    This function uses a sliding window technique to find the longest substring without repeating characters.
    It maintains a dictionary to keep track of the last occurrence of each character.
    The window is represented by two pointers, start and end, which are the start and end of the window respectively.
    The function iterates over the string with the end pointer. If the current character is not in the used_chars
    dictionary or if it is in the dictionary but its last occurrence is not in the current window (i.e., start > used_chars[s[
    end]]),
    the window expands by moving the end pointer to the right. If the current character is in the used_chars dictionary and
    its last occurrence is in the current window (i.e., start <= used_chars[s[end]]), the window contracts by moving the start
    pointer to the right of the last occurrence of the current character. The length of the longest window encountered during
    this process is stored in max_length and represents the length of the longest substring without repeating characters.

    Args:
        s (str): The input string.

    Returns:
        tuple[int, str]: A tuple containing the length of the longest substring without repeating characters and the substring
        itself.

    Examples:
        >>> method_00('abcabcbb')
        (3, 'abc')

        >>> method_00('bbbbbb')
        (1, 'b')

        >>> method_00('pwwkew')
        (3, 'wke')
    """
    start = 0
    max_length = 0
    used_chars = {}

    for end in range(len(s)):
        if s[end] in used_chars and start <= used_chars[s[end]]:
            start = used_chars[s[end]] + 1
        else:
            max_length = max(max_length, end - start + 1)

        used_chars[s[end]] = end

    return max_length, s[start : start + max_length]


if __name__ == '__main__':
    print(__doc__)
