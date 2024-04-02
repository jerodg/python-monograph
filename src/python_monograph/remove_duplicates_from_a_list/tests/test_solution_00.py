#!/usr/bin/env python3
"""Python Monograph: Remove Duplicates from a Sorted Array Solution 00 Tests

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

from src.python.remove_duplicates_from_a_list.solution_00 import solution_00


def test_solution_00_removes_duplicates():
    assert solution_00([1, 2, 2, 3, 4, 4, 5, 6, 6]) == [1, 2, 3, 4, 5, 6]


def test_solution_00_handles_empty_list():
    assert solution_00([]) == []


def test_solution_00_handles_single_element_list():
    assert solution_00([1]) == [1]


def test_solution_00_handles_all_duplicates():
    assert solution_00([1, 1, 1, 1]) == [1]


# def test_solution_00_handles_large_input():
#     assert solution_00(list(range(1000000))) == list(range(1000000))


@pytest.mark.parametrize('input_list', [[1, 2, 3], [4, 5, 6], [7, 8, 9]])
def test_solution_00_handles_multiple_inputs(input_list):
    assert solution_00(input_list) == set(input_list)


def test_solution_00_handles_random_order():
    assert solution_00([3, 2, 1]) == {1, 2, 3}


def test_solution_00_handles_special_characters():
    assert solution_00(['a', 'b', 'b', 'c']) == {'a', 'b', 'c'}


def test_solution_00_handles_negative_numbers():
    assert solution_00([-1, -2, -2, -3]) == {-1, -2, -3}


def test_solution_00_regression_test():
    assert solution_00([1, 2, 2, 3, 4, 4, 5, 6, 6]) == {1, 2, 3, 4, 5, 6}


def test_solution_00_equivalence_partitioning():
    assert solution_00([1, 2, 3]) == {1, 2, 3}
    assert solution_00([4, 5, 6]) == {4, 5, 6}
    assert solution_00([7, 8, 9]) == {7, 8, 9}


if __name__ == '__main__':
    print(__doc__)
