"""
Python Monograph -> Sorting for Humans (Natural Sort) -> Solution 03 -> Tests

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

import pytest
from pytest_benchmark.plugin import benchmark

from python_monograph.natural_sort.solution_03 import natural_sort


def test_natural_sort_with_files():
    assert natural_sort(['file1.txt', 'file10.txt', 'file2.txt']) == ['file1.txt', 'file2.txt', 'file10.txt']


def test_natural_sort_with_images():
    assert natural_sort(['image99.png', 'image100.png', 'image101.png', 'image1.png', 'image10.png']) == ['image1.png',
                                                                                                          'image10.png',
                                                                                                          'image99.png',
                                                                                                          'image100.png',
                                                                                                          'image101.png']


def test_natural_sort_with_versions():
    assert natural_sort(['version1.10', 'version1.2', 'version1.1']) == ['version1.1', 'version1.2', 'version1.10']


def test_natural_sort_with_empty_list():
    assert natural_sort([]) == []


def test_natural_sort_with_single_element():
    assert natural_sort(['single']) == ['single']


def test_natural_sort_with_same_elements():
    assert natural_sort(['same', 'same', 'same']) == ['same', 'same', 'same']


def test_natural_sort_with_special_characters():
    assert natural_sort(['file#1', 'file#2', 'file#10']) == ['file#1', 'file#2', 'file#10']


def test_natural_sort_with_leading_zeros():
    assert natural_sort(['file001', 'file010', 'file100']) == ['file001', 'file010', 'file100']


@pytest.mark.benchmark
def test_natural_sort_with_large_input(benchmark):
    large_input = ['file{}'.format(i) for i in range(100000)]
    benchmark(natural_sort, large_input)


@pytest.mark.random
def test_natural_sort_with_random_input():
    random_input = ['file{}'.format(random.randint(1, 100)) for _ in range(1000)]
    assert natural_sort(random_input) == sorted(random_input, key=lambda s: int(s[4:]))


def test_natural_sort_with_duplicates():
    assert natural_sort(['file1', 'file1', 'file2']) == ['file1', 'file1', 'file2']


def test_natural_sort_with_no_duplicates():
    assert natural_sort(['file1', 'file2', 'file3']) == ['file1', 'file2', 'file3']


def test_natural_sort_preserves_order():
    assert natural_sort(['file1', 'file2', 'file2']) == ['file1', 'file2', 'file2']


def test_natural_sort_with_non_string_input():
    with pytest.raises(TypeError):
        natural_sort([1, 2, 3])
