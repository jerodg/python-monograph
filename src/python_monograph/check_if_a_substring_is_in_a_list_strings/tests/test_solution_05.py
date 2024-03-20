#!/usr/bin/env python3
"""Python Monograph: Check if a Substring is in a List of Strings Solution 05 Tests

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

import pytest

from check_if_a_substring_is_in_a_list_strings import solution_05


def test_substring_found_in_list():
    assert solution_05(['apple', 'banana', 'cherry'], 'app') == True


def test_substring_not_found_in_list():
    assert solution_05(['apple', 'banana', 'cherry'], 'z') == False


def test_substring_found_in_one_string_only():
    assert solution_05(['apple', 'banana', 'cherry'], 'ban') == True


def test_substring_found_in_all_strings():
    assert solution_05(['apple', 'banana', 'cherry'], 'a') == True


def test_substring_is_empty_string():
    assert solution_05(['apple', 'banana', 'cherry'], '') == True


def test_list_is_empty():
    assert solution_05([], 'app') == False


def test_list_contains_empty_string():
    assert solution_05(['apple', '', 'cherry'], 'app') == True


def test_list_contains_only_empty_strings():
    assert solution_05(['', '', ''], 'app') == False


def test_list_contains_none():
    with pytest.raises(TypeError):
        solution_05(['apple', None, 'cherry'], 'app')


def test_substring_is_none():
    with pytest.raises(TypeError):
        solution_05(['apple', 'banana', 'cherry'], None)


def test_list_contains_non_string_elements():
    with pytest.raises(TypeError):
        solution_05(['apple', 123, 'cherry'], 'app')


def test_list_contains_strings_with_special_characters():
    assert solution_05(['app$le', 'banana', 'cherry'], '$') == True


def test_substring_contains_special_characters():
    assert solution_05(['apple', 'banana', 'cherry'], '$') == False


def test_list_contains_strings_with_numbers():
    assert solution_05(['apple1', 'banana', 'cherry'], '1') == True


def test_substring_contains_numbers():
    assert solution_05(['apple', 'banana', 'cherry'], '1') == False
