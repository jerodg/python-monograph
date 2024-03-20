#!/usr/bin/env python3
"""Python Monograph: Check if an Array is Monotonic Solution 00 Tests

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
from src.python import solution_00


def test_solution_00_increasing_sequence_returns_true():
    assert solution_00([1, 2, 3, 4, 5]) is True


def test_solution_00_decreasing_sequence_returns_true():
    assert solution_00([5, 4, 3, 2, 1]) is True


def test_solution_00_non_monotonic_sequence_returns_false():
    assert solution_00([1, 2, 3, 2, 1]) is False


def test_solution_00_empty_sequence_returns_true():
    assert solution_00([]) is True


def test_solution_00_single_element_sequence_returns_true():
    assert solution_00([1]) is True


def test_solution_00_sequence_with_same_elements_returns_true():
    assert solution_00([2, 2, 2, 2, 2]) is True


def test_solution_00_sequence_with_negative_numbers_returns_true():
    assert solution_00([-1, -2, -3, -4, -5]) is True


def test_solution_00_sequence_with_mixed_positive_and_negative_numbers_returns_false():
    assert solution_00([-1, -2, 3, 4, 5]) is False


if __name__ == '__main__':
    print(__doc__)
