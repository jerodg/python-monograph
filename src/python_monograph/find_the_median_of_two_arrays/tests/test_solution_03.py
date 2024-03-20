#!/usr/bin/env python3
"""Python Monograph: Find the Median of Two Arrays Solution 03 Tests

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

from find_the_median_of_two_arrays import solution_03


def test_median_of_sorted_arrays_with_odd_length():
    assert solution_03([1, 3, 5], [2, 4, 6]) == 3.5


def test_median_of_sorted_arrays_with_even_length():
    assert solution_03([1, 2], [3, 4]) == 2.5


def test_median_of_sorted_arrays_with_negative_numbers():
    assert solution_03([-1, -3, -5], [-2, -4, -6]) == -3.5


def test_median_of_sorted_arrays_with_zeroes():
    assert solution_03([0, 0, 0], [0, 0, 0]) == 0.0


def test_median_of_sorted_arrays_with_one_array_empty():
    assert solution_03([], [1, 2, 3, 4, 5]) == 3.0


def test_median_of_sorted_arrays_with_both_arrays_empty():
    with pytest.raises(ValueError):
        solution_03([], [])


def test_median_of_sorted_arrays_with_one_element_each():
    assert solution_03([1], [2]) == 1.5


def test_median_of_sorted_arrays_with_same_elements():
    assert solution_03([1, 1, 1, 1], [1, 1, 1, 1]) == 1.0


if __name__ == '__main__':
    print(__doc__)
