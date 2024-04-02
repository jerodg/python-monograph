"""
Python Monograph -> Calculate Product Sum from Nested Array -> Solution 00 -> Tests

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

from src.python_monograph.calculate_product_sum_from_nested_array.solution_00 import calculate_product_sum


def test_calculate_product_sum_with_single_level_list():
    assert calculate_product_sum([1, 2, 3, 4, 5]) == 15


def test_calculate_product_sum_with_two_level_list():
    assert calculate_product_sum([1, 2, [3, 4]]) == 14


def test_calculate_product_sum_with_five_level_list():
    assert calculate_product_sum([1, [2, [3, [4, [5]]]]]) == 105


def test_calculate_product_sum_with_multiple_sublists():
    assert calculate_product_sum([[1, 2], [3, 4], [5, 6]]) == 42


def test_calculate_product_sum_with_empty_list():
    assert calculate_product_sum([]) == 0


def test_calculate_product_sum_with_single_element():
    assert calculate_product_sum([1]) == 1


def test_calculate_product_sum_with_large_numbers():
    assert calculate_product_sum([10 ** 6, [10 ** 6, [10 ** 6]]]) == 3000000


def test_calculate_product_sum_with_large_list():
    assert calculate_product_sum([1] * 10 ** 4) == 10 ** 4


def test_calculate_product_sum_with_large_depth():
    assert calculate_product_sum([1, [1, [1, [1, [1, [1, [1, [1, [1, [1, [1]]]]]]]]]]]) == 55


def test_calculate_product_sum_with_negative_numbers():
    assert calculate_product_sum([-1, 2, [-3, 4]]) == 6


def test_calculate_product_sum_with_zero():
    assert calculate_product_sum([0, 1, [2, 3]]) == 7


def test_calculate_product_sum_with_non_integer_elements():
    with pytest.raises(TypeError):
        calculate_product_sum([1, 2, [3, '4']])


def test_calculate_product_sum_with_depth_exceeding_ten():
    with pytest.raises(RecursionError):
        calculate_product_sum([1] * 11)


@pytest.mark.benchmark
def test_calculate_product_sum_performance(benchmark):
    benchmark(calculate_product_sum, ([1] * 10 ** 4))
