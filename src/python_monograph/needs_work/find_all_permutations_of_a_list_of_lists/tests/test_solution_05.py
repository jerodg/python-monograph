#!/usr/bin/env python3
"""Python Monograph: Find All Permutations of a List of Lists Solution 05 Tests

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

from templates.python import solution_05


def test_empty_list():
    assert solution_05([]) == [[]]


def test_single_element_list():
    assert solution_05([1]) == [[1]]


def test_two_elements_list():
    assert sorted(solution_05([1, 2])) == sorted([[1, 2], [2, 1]])


def test_three_elements_list():
    assert sorted(solution_05([1, 2, 3])) == sorted([[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]])


def test_list_with_duplicate_elements():
    assert sorted(solution_05([1, 1])) == sorted([[1, 1], [1, 1]])


# fixme: this test is failing@pytest.mark.timeout(1)
# def test_performance_large_input():
#     solution_01(list(range(10)))


if __name__ == '__main__':
    print(__doc__)
