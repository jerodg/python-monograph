#!/usr/bin/env python3
"""Python Monograph: Find Triplets With Zero Sum Solution 01 Tests

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
from find_triplets_with_zero_sum import solution_01


def test_triplets_with_zero_sum_happy_path():
    assert solution_01([0, -1, 2, -3, 1]) == [[-3, 1, 2], [-1, 0, 1]]


def test_triplets_with_zero_sum_no_triplets():
    assert solution_01([0, -1, 2, -3]) == []


def test_triplets_with_zero_sum_all_zeros():
    assert solution_01([0, 0, 0, 0]) == [[0, 0, 0]]


def test_triplets_with_zero_sum_all_positive():
    assert solution_01([1, 2, 3, 4]) == []


def test_triplets_with_zero_sum_all_negative():
    assert solution_01([-1, -2, -3, -4]) == []


def test_triplets_with_zero_sum_large_numbers():
    assert solution_01([1000000, 2000000, -3000000]) == [[-3000000, 1000000, 2000000]]


def test_triplets_with_zero_sum_small_numbers():
    assert solution_01([0.000001, -0.000002, 0.000001]) == [[-0.000002, 0.000001, 0.000001]]


def test_triplets_with_zero_sum_empty_list():
    assert solution_01([]) == []


if __name__ == '__main__':
    print(__doc__)
