"""
Python Monograph -> Find a Substring Within a List of Strings -> Solution 07 -> Tests

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

from python_monograph.find_substring_within_a_list_of_strings.solution_07 import find_substring


def test_find_substring_with_valid_input():
    assert find_substring(["hello", "world", "python", "programming"], "pyt") == 2


def test_find_substring_with_invalid_input():
    assert find_substring(["hello", "world", "python", "programming"], "java") is None


def test_find_substring_with_duplicate_strings():
    assert find_substring(["hello", "hello", "world", "python", "programming"], "hello") == 0


def test_find_substring_with_empty_target_string():
    with pytest.raises(ValueError):
        find_substring(["hello", "world", "python", "programming"], "")


def test_find_substring_with_empty_list():
    with pytest.raises(ValueError):
        find_substring([], "hello")


def test_find_substring_with_special_characters():
    assert find_substring(["hello", "world", "@python", "programming"], "@python") == 2


def test_find_substring_with_case_sensitivity():
    assert find_substring(["hello", "world", "Python", "programming"], "python") is None


def test_find_substring_with_random_order():
    assert find_substring(["world", "hello", "python", "programming"], "hello") == 1


def test_find_substring_with_order_preservation():
    assert find_substring(["hello", "world", "python", "programming"], "programming") == 3


def test_find_substring_with_equivalence_partitioning():
    assert find_substring(["hello", "world", "python", "programming"], "world") == 1


# todo: This needs to be reworked
# def test_find_substring_with_security():
#     assert find_substring(["hello", "world", "python", "programming"], "world") == 1


def test_find_substring_with_functional():
    assert find_substring(["hello", "world", "python", "programming"], "world") == 1


def test_find_substring_with_no_duplicates():
    assert find_substring(["hello", "world", "python", "programming"], "world") == 1


def test_find_substring_with_duplicates():
    assert find_substring(["hello", "world", "world", "python", "programming"], "world") == 1


@pytest.mark.benchmark
def test_find_substring_with_large_inputs(benchmark):
    large_list = ["a" * 100000] * 100000
    benchmark(find_substring, large_list, "a")
