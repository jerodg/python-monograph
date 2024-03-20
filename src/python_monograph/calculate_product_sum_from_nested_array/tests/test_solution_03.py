#!/usr/bin/env python3
"""Python Monograph: Calculate Product Sum of a Nested Array Solution 03 Tests

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

from templates.python import iterate, solution_03


def test_iterate_flat_array():
    assert list(iterate([1, 2, 3])) == [(1, 1), (2, 1), (3, 1)]


def test_iterate_nested_array():
    assert list(iterate([-1, 2, [-3, 4]])) == [(-1, 1), (2, 1), (-3, 2), (4, 2)]


def test_product_sum_of_flat_array():
    assert solution_03([1, 2, 3]) == 6


def test_product_sum_of_nested_array():
    assert solution_03([-1, 2, [-3, 4]]) == 3


def test_product_sum_with_large_depth():
    assert solution_03([1, 2, 3, [4, 5]]) == 24


def test_product_sum_of_array_with_negative_numbers():
    assert solution_03([1, -1]) == 0


def test_product_sum_of_array_with_negative_and_positive_numbers():
    assert solution_03([1, -2]) == -1


def test_product_sum_of_array_with_floats():
    assert solution_03([-3.5, [1, [0.5]]]) == 0


@pytest.mark.parametrize('arr', [([1, 2, 3], 1000000), ([1, 2, 3], 0.000001)])
def test_product_sum_performance(arr):
    assert solution_03(arr) is not None


@pytest.mark.parametrize('arr', [([1, 2, 3], 0), ([1, 2, 3], 1), ([1, 2, 3], -1)])
def test_product_sum_random(arr):
    assert solution_03(arr) is not None


def test_product_sum_of_empty_array():
    assert solution_03([]) == 0


def test_product_sum_of_array_with_invalid_elements():
    with pytest.raises(TypeError):
        solution_03([1, 'a', 3])


if __name__ == '__main__':
    print(__doc__)
