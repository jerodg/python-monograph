#!/usr/bin/env python3
"""Python Monograph: Test

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

from index_2d_array_in_1d.solution_00 import Index2DArrayIterator, index_2d_array_in_1d


def test_index_2d_array_in_1d_with_valid_index():
    assert index_2d_array_in_1d([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 4) == 5


def test_index_2d_array_in_1d_with_zero_index():
    assert index_2d_array_in_1d([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 0) == 1


def test_index_2d_array_in_1d_with_last_index():
    assert index_2d_array_in_1d([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 8) == 9


def test_index_2d_array_in_1d_with_empty_array():
    with pytest.raises(ValueError, match='no items in array'):
        index_2d_array_in_1d([[]], 0)


def test_index_2d_array_in_1d_with_negative_index():
    with pytest.raises(ValueError, match='index out of range'):
        index_2d_array_in_1d([[1, 2, 3], [4, 5, 6], [7, 8, 9]], -1)


def test_index_2d_array_in_1d_with_index_out_of_range():
    with pytest.raises(ValueError, match='index out of range'):
        index_2d_array_in_1d([[1, 2, 3], [4, 5, 6], [7, 8, 9]], 9)


def test_index_2d_array_iterator_with_valid_matrix():
    assert list(Index2DArrayIterator([[1, 2, 3], [4, 5, 6], [7, 8, 9]])) == [1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_index_2d_array_iterator_with_empty_matrix():
    assert list(Index2DArrayIterator([[]])) == []


def test_index_2d_array_iterator_with_single_element_matrix():
    assert list(Index2DArrayIterator([[1]])) == [1]


if __name__ == '__main__':
    print(__doc__)
