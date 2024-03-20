#!/usr/bin/env python3
"""Python Monograph: Find Pairs With the Given Sum Solution 03 Tests

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
from find_pairs_with_given_sum import solution_03


def test_solution_03_with_positive_numbers():
    assert solution_03([1, 5, 7, 1], 6) == (2, [(1, 5), (1, 5)])


def test_solution_03_with_same_numbers():
    assert solution_03([1, 1, 1, 1, 1, 1, 1, 1], 2) == (7, [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])


def test_solution_03_with_no_pairs():
    assert solution_03([1, 2, 3, 4, 5], 10) == (0, [])


def test_solution_03_with_negative_numbers():
    assert solution_03([-1, -2, -3, -4, -5], -3) == (1, [(-2, -1)])


def test_solution_03_with_mixed_numbers():
    assert solution_03([-1, 2, 3, -4, 5], 1) == (2, [(-4, 5), (-1, 2)])


def test_solution_03_with_empty_list():
    assert solution_03([], 1) == (0, [])


def test_solution_03_with_large_numbers():
    assert solution_03([10**6, 10**6, 10**6], 2 * 10**6) == (2, [(1000000, 1000000), (1000000, 1000000)])


# fixme: benchmarking not working
# @pytest.mark.performance
# def test_solution_03_performance(benchmark):
#     benchmark(solution_03, [1] * 10**6, 2)
if __name__ == '__main__':
    print(__doc__)
