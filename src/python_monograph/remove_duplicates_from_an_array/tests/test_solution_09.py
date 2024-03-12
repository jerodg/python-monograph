"""
Python Monograph -> Remove Duplicates from an Array -> Solution 09 -> Tests

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

from python_monograph.remove_duplicates_from_an_array.solution_09 import remove_duplicates


def test_remove_duplicates_with_integers():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]


def test_remove_duplicates_with_strings():
    assert sorted(remove_duplicates(['a', 'b', 'b', 'c', 'd', 'd', 'e', 'e'])) == sorted(['d', 'c', 'e', 'b', 'a'])


def test_remove_duplicates_with_empty_list():
    assert remove_duplicates([]) == []


def test_remove_duplicates_with_no_duplicates():
    assert remove_duplicates([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_remove_duplicates_with_all_duplicates():
    assert remove_duplicates([1, 1, 1, 1, 1]) == [1]


def test_remove_duplicates_with_large_input():
    large_input = list(range(100000)) * 2
    assert remove_duplicates(large_input) == list(range(100000))


def test_remove_duplicates_with_random_input():
    random_input = [random.choice(string.ascii_letters) for _ in range(1000)]
    assert remove_duplicates(random_input) == list(set(random_input))


def test_remove_duplicates_with_special_characters():
    assert sorted(remove_duplicates(['!', '@', '@', '#', '$', '$', '%', '^', '^'])) == sorted(
        ['!', '@', '#', '$', '%', '^'])


def test_remove_duplicates_does_not_preserve_order():
    assert remove_duplicates([3, 2, 1, 2, 3]) != [3, 2, 1]


def test_remove_duplicates_equivalence_partitioning():
    assert sorted(remove_duplicates([1, 2, 2, 3, 4, 4, 5, 5])) == sorted([1, 2, 3, 4, 5])
    assert sorted(remove_duplicates(['a', 'b', 'b', 'c', 'd', 'd', 'e', 'e'])) == sorted(['a', 'b', 'c', 'd', 'e'])
    assert sorted(remove_duplicates([])) == sorted([])
    assert sorted(remove_duplicates([1, 2, 3, 4, 5])) == sorted([1, 2, 3, 4, 5])
    assert sorted(remove_duplicates([1, 1, 1, 1, 1])) == sorted([1])


def test_remove_duplicates_security():
    with pytest.raises(TypeError):
        remove_duplicates(None)


def test_remove_duplicates_functionality():
    assert remove_duplicates([1, 2, 2, 3, 4, 4, 5, 5]) == [1, 2, 3, 4, 5]


@pytest.mark.benchmark
def test_remove_duplicates_performance(benchmark):
    large_input = list(range(100000)) * 2
    benchmark(remove_duplicates, large_input)
