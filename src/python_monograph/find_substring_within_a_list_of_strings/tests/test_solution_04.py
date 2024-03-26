"""
Python Monograph -> Find a Substring Within a List of Strings -> Solution 04 -> Tests

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

from python_monograph.find_substring_within_a_list_of_strings.solution_04 import SuffixArray


# fixme: This is returning a bool instead of the index of the pattern.

def test_find_substring_returns_true_when_pattern_exists():
    sa = SuffixArray(["hello", "world", "python", "programming"])
    assert sa.find_substring("hell") is True


def test_find_substring_returns_false_when_pattern_does_not_exist():
    sa = SuffixArray(["hello", "world", "python", "programming"])
    assert sa.find_substring("java") is False


def test_find_substring_returns_true_when_pattern_is_empty_string():
    sa = SuffixArray(["hello", "world", "python", "programming"])
    assert sa.find_substring("") is True


def test_find_substring_returns_true_when_pattern_is_in_multiple_strings():
    sa = SuffixArray(["hello", "world", "python", "programming"])
    assert sa.find_substring("o") is True


def test_find_substring_returns_false_when_strings_list_is_empty():
    sa = SuffixArray([])
    assert sa.find_substring("hello") is False


def test_find_substring_returns_true_when_pattern_is_full_string():
    sa = SuffixArray(["hello", "world", "python", "programming"])
    assert sa.find_substring("hello") is True


def test_find_substring_returns_true_when_pattern_is_duplicate_in_string():
    sa = SuffixArray(["hello", "hello", "world", "python", "programming"])
    assert sa.find_substring("hello") is True


def test_find_substring_returns_false_when_pattern_is_longer_than_strings():
    sa = SuffixArray(["hello", "world", "python", "programming"])
    assert sa.find_substring("helloworld") is False


def test_find_substring_returns_true_when_pattern_is_special_character():
    sa = SuffixArray(["hello", "world", "#python", "programming"])
    assert sa.find_substring("#") is True


def test_find_substring_returns_true_when_pattern_is_number():
    sa = SuffixArray(["hello", "world", "python3", "programming"])
    assert sa.find_substring("3") is True


def test_find_substring_returns_true_when_pattern_is_case_sensitive():
    sa = SuffixArray(["hello", "world", "Python", "programming"])
    assert sa.find_substring("Python") is True
    assert sa.find_substring("python") is False


@pytest.mark.benchmark
def test_find_substring_with_large_inputs(benchmark):
    large_list = ["a" * 100000]
    sa = SuffixArray(large_list)
    benchmark(sa.find_substring, "a")
