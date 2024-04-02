"""
Python Monograph -> Split Strings into Groups of n Consecutive Characters -> Solution 12 -> Tests

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

from python_monograph.split_string_into_groups_of_n_consecutive_characters.solution_12 import split_string_into_groups


def test_split_string_into_groups_with_valid_input():
    assert split_string_into_groups("HelloWorld", 3) == ["Hel", "loW", "orl", "d"]


def test_split_string_into_groups_with_boundary_input():
    assert split_string_into_groups("Python", 2) == ["Py", "th", "on"]


def test_split_string_into_groups_with_edge_case_input():
    assert split_string_into_groups("1234567890", 4) == ["1234", "5678", "90"]


def test_split_string_into_groups_with_performance_input():
    assert split_string_into_groups("a" * 1000000, 500000) == ["a" * 500000, "a" * 500000]


def test_split_string_into_groups_with_random_input():
    assert split_string_into_groups("abc", 1) == ["a", "b", "c"]


def test_split_string_into_groups_with_special_case_input():
    assert split_string_into_groups("abc", 5) == ["abc"]


def test_split_string_into_groups_with_validation_input():
    with pytest.raises(ValueError):
        split_string_into_groups("abc", 0)


def test_split_string_into_groups_with_regression_input():
    assert split_string_into_groups("HelloWorld", 3) == ["Hel", "loW", "orl", "d"]


def test_split_string_into_groups_with_equivalence_partitioning_input():
    assert split_string_into_groups("abcabc", 3) == ["abc", "abc"]


def test_split_string_into_groups_with_security_input():
    assert split_string_into_groups("abc; drop table users;", 4) == ["abc;", " dro", "p ta", "ble ", "user", "s;"]


def test_split_string_into_groups_with_functional_input():
    assert split_string_into_groups("HelloWorld", 3) == ["Hel", "loW", "orl", "d"]


def test_split_string_into_groups_with_duplicates_input():
    assert split_string_into_groups("abcabc", 3) == ["abc", "abc"]


def test_split_string_into_groups_with_no_duplicates_input():
    assert split_string_into_groups("abcdef", 3) == ["abc", "def"]


def test_split_string_into_groups_with_order_preservation_input():
    assert split_string_into_groups("abcdef", 3) == ["abc", "def"]
