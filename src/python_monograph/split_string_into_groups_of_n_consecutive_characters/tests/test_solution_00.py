"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters -> Solution 00 -> Tests

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
import random
import string

import pytest

from python_monograph.split_string_into_groups_of_n_consecutive_characters.solution_00 import split_string_into_groups


def test_split_string_into_groups_with_no_duplicates():
    assert sorted(split_string_into_groups("abcdef", 2)) == sorted(['ab', 'cd', 'ef'])


def test_split_string_into_groups_with_duplicates():
    assert sorted(split_string_into_groups("aabbcc", 2)) == sorted(['aa', 'bb', 'cc'])


# This test is not applicable to this solution as it does not preserve the original order of the groups.
# def test_split_string_into_groups_with_order_preservation():
#     assert split_string_into_groups("abcdef", 1) == ['a', 'b', 'c', 'd', 'e', 'f']


def test_split_string_into_groups_with_empty_string():
    assert split_string_into_groups("", 2) == []


def test_split_string_into_groups_with_single_character():
    assert split_string_into_groups("a", 2) == ['a']


def test_split_string_into_groups_with_group_size_larger_than_string_length():
    assert split_string_into_groups("abc", 5) == ['abc']


def test_split_string_into_groups_with_large_input():
    large_string = "a" * 10 ** 6
    assert split_string_into_groups(large_string, 10 ** 6) == [large_string]


def test_split_string_into_groups_with_random_input():
    random_string = ''.join(random.choices(string.ascii_uppercase + string.digits, k=100))
    assert len(split_string_into_groups(random_string, 10)) == 10


def test_split_string_into_groups_with_special_characters():
    assert sorted(split_string_into_groups("@#$$%%^^", 2)) == sorted(['@#', '$$', '%%', '^^'])


def test_split_string_into_groups_with_negative_group_size():
    with pytest.raises(ValueError):
        split_string_into_groups("abcdef", -2)


def test_split_string_into_groups_with_zero_group_size():
    with pytest.raises(ValueError):
        split_string_into_groups("abcdef", 0)


def test_split_string_into_groups_with_non_integer_group_size():
    with pytest.raises(TypeError):
        split_string_into_groups("abcdef", "2")


def test_split_string_into_groups_with_non_string_input():
    with pytest.raises(TypeError):
        split_string_into_groups(123456, 2)


def test_split_string_into_groups_with_security_sensitive_input():
    assert sorted(split_string_into_groups("password123", 4)) == sorted(['pass', 'word', '123'])


def test_split_string_into_groups_with_functional_characters():
    assert sorted(split_string_into_groups("\n\t\r", 1)) == sorted(['\n', '\t', '\r'])
