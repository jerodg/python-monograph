#!/usr/bin/env python3
"""Python Monograph: Merge Sorted Arrays Solution 05 Tests

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

from templates.python import solution_05


def test_merge_sorted_arrays_happy_path():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    assert solution_05(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]


def test_merge_sorted_arrays_boundary_case():
    nums1 = [1, 0]
    m = 1
    nums2 = [2]
    n = 1
    assert solution_05(nums1, m, nums2, n) == [1, 2]


def test_merge_sorted_arrays_edge_case():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = []
    n = 0
    assert solution_05(nums1, m, nums2, n) == [1, 2, 3]


@pytest.mark.benchmark
def test_merge_sorted_arrays_solution_05(benchmark):
    nums1 = list(range(1, 100000)) + [0] * 100000
    m = 100000
    nums2 = list(range(100001, 200001))
    n = 100000
    benchmark(solution_05, nums1, m, nums2, n)  # assert solution_05(nums1, m, nums2, n) == list(range(1, 200001))


def test_merge_sorted_arrays_special_case():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    assert solution_05(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]


def test_merge_sorted_arrays_validation():
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    assert solution_05(nums1, m, nums2, n) == [1, 2, 2, 3, 5, 6]


if __name__ == '__main__':
    print(__doc__)
