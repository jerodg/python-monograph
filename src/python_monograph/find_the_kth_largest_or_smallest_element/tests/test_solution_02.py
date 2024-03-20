#!/usr/bin/env python3
"""Python Monograph: Find the kth Largest or Smallest Element Solution 02 Tests

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

from find_the_kth_largest_or_smallest_element.solution_02 import solution_02


def test_kth_largest_element():
    assert solution_02([3, 2, 1, 5, 6, 4], 2) == 5


def test_kth_smallest_element():
    assert solution_02([3, 2, 1, 5, 6, 4], 2, largest=False) == 2


def test_kth_element_with_duplicates():
    assert solution_02([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4


def test_kth_element_with_negative_numbers():
    assert solution_02([-3, -2, -1, -5, -6, -4], 2) == -2


def test_kth_element_with_empty_list():
    with pytest.raises(IndexError):
        solution_02([], 2)


def test_kth_element_with_k_larger_than_list_length():
    with pytest.raises(IndexError):
        solution_02([1, 2, 3], 5)


def test_kth_element_with_k_zero():
    with pytest.raises(IndexError):
        solution_02([1, 2, 3], 0)


def test_kth_element_with_k_negative():
    with pytest.raises(IndexError):
        solution_02([1, 2, 3], -1)


if __name__ == '__main__':
    print(__doc__)
