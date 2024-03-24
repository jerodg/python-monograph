"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters -> Solution 13 -> Tests

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
import pytest

from python_monograph.split_string_into_groups_of_n_consecutive_characters.solution_13 import split_string_into_groups


def test_split_string_into_groups_with_valid_input():
    assert split_string_into_groups("HelloWorld", 3) == ["Hel", "loW", "orl", "d"]


def test_split_string_into_groups_with_single_character_groups():
    assert split_string_into_groups("abc", 1) == ["a", "b", "c"]


def test_split_string_into_groups_with_group_size_larger_than_string_length():
    assert split_string_into_groups("abc", 5) == ["abc"]


def test_split_string_into_groups_with_empty_string():
    assert split_string_into_groups("", 3) == ['']


def test_split_string_into_groups_with_zero_group_size():
    with pytest.raises(ValueError):
        split_string_into_groups("abc", 0)


def test_split_string_into_groups_with_negative_group_size():
    with pytest.raises(ValueError):
        split_string_into_groups("abc", -1)


def test_split_string_into_groups_with_large_input():
    large_string = "a" * 10 ** 6
    result = split_string_into_groups(large_string, 10 ** 5)
    assert len(result) == 10
    assert all(len(group) == 10 ** 5 for group in result)


def test_split_string_into_groups_with_random_input():
    import random
    import string
    random_string = ''.join(random.choices(string.ascii_letters + string.digits, k=100))
    result = split_string_into_groups(random_string, 10)
    assert len(result) == 10
    assert all(len(group) == 10 for group in result)


def test_split_string_into_groups_with_special_characters():
    assert split_string_into_groups("!@#$%^&*()", 2) == ["!@", "#$", "%^", "&*", "()"]


def test_split_string_into_groups_with_duplicates():
    assert split_string_into_groups("aaabbbccc", 3) == ["aaa", "bbb", "ccc"]


def test_split_string_into_groups_without_duplicates():
    assert split_string_into_groups("abcabcabc", 3) == ["abc", "abc", "abc"]


def test_split_string_into_groups_order_preservation():
    assert split_string_into_groups("cba", 1) == ["c", "b", "a"]
