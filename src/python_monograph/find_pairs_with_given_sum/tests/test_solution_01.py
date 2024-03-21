#!/usr/bin/env python3
"""Python Monograph: Find Pairs With the Given Sum Solution 01 Tests

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
from find_pairs_with_given_sum.solution_01 import solution_01


def test_solution_01_with_positive_numbers():
    assert solution_01([1, 5, 7, 1], 6) == (2, [(5, 1), (1, 5)])


def test_solution_01_with_same_numbers():
    assert solution_01([1, 1, 1, 1, 1, 1, 1, 1], 2) == (28, [(1, 1)] * 28)


def test_solution_01_with_no_pairs():
    assert solution_01([1, 2, 3, 4, 5], 10) == (0, [])


def test_solution_01_with_negative_numbers():
    assert solution_01([-1, -2, -3, -4, -5], -3) == (1, [(-2, -1)])


def test_solution_01_with_mixed_numbers():
    assert solution_01([-1, 2, 3, -4, 5], 1) == (2, [(2, -1), (5, -4)])


def test_solution_01_with_empty_list():
    assert solution_01([], 1) == (0, [])


def test_solution_01_with_large_numbers():
    assert solution_01([10 ** 6, 10 ** 6, 10 ** 6], 2 * 10 ** 6) == (3, [(10 ** 6, 10 ** 6)] * 3)


# fixme: benchmarking not working
# @pytest.mark.performance
# def test_solution_01_performance(benchmark):
#     benchmark(solution_01, [1] * 10**6, 2)


if __name__ == '__main__':
    print(__doc__)
