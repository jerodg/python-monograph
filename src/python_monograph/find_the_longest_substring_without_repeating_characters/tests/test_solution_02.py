#!/usr/bin/env python3
"""Python Monograph: Find the Longest Substring Without Repeating Characters Solution 02 Test

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
from find_the_longest_substring_without_repeating_characters.solution_02 import solution_02


def test_longest_substring_with_all_unique_characters():
    assert solution_02('abcde') == (5, 'abcde')


def test_longest_substring_with_all_same_characters():
    assert solution_02('aaaaa') == (1, 'a')


def test_longest_substring_with_repeating_characters():
    assert solution_02('abcabcbb') == (3, 'abc')


def test_longest_substring_with_empty_string():
    assert solution_02('') == (0, '')


def test_longest_substring_with_one_character():
    assert solution_02('a') == (1, 'a')


def test_longest_substring_with_two_different_characters():
    assert solution_02('ab') == (2, 'ab')


def test_longest_substring_with_two_same_characters():
    assert solution_02('aa') == (1, 'a')


def test_longest_substring_with_special_characters():
    assert solution_02('!@#$%^&*()') == (10, '!@#$%^&*()')


def test_longest_substring_with_numbers():
    assert solution_02('1234567890') == (10, '1234567890')


def test_longest_substring_with_mixed_characters():
    assert solution_02('a1b2c3d4e5') == (10, 'a1b2c3d4e5')


if __name__ == '__main__':
    print(__doc__)
