"""
Python Monograph -> Find All Permutations of a List, Set, or Tuple  -> Solution 00 -> Tests

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
If not, see <https://www.mongodb.com/licensing/server-side-public-license>.
"""
import pytest

from python_monograph.find_all_permutations_of_a_list_set_or_tuple.solution_00 import find_all_permutations


def test_empty_input():
    assert find_all_permutations([]) == []


def test_single_list_input():
    assert find_all_permutations([1, 2, 3]) == [[1], [2], [3]]


# def test_single_list_input_():
#     assert find_all_permutations([[1, 3, 4], [6, 7, 9], [8, 10, 5]]) == [[1, 6, 8], [1, 6, 10], [1, 6, 5], [1, 7, 8],
#                                                                      [1, 7, 10], [1, 7, 5], [1, 9, 8], [1, 9, 10],
#                                                                      [1, 9, 5], [3, 6, 8], [3, 6, 10], [3, 6, 5],
#                                                                      [3, 7, 8], [3, 7, 10], [3, 7, 5], [3, 9, 8],
#                                                                      [3, 9, 10], [3, 9, 5], [4, 6, 8], [4, 6, 10],
#                                                                      [4, 6, 5], [4, 7, 8], [4, 7, 10], [4, 7, 5],
#                                                                      [4, 9, 8], [4, 9, 10], [4, 9, 5]]


def test_multiple_lists_input():
    assert find_all_permutations([[1, 2], [3, 4]]) == [[1, 3], [3, 1], [1, 4], [4, 1], [2, 3], [3, 2], [2, 4], [4, 2]]


def test_input_with_empty_lists():
    assert find_all_permutations([[1, 2], [], [3, 4]]) == []


def test_input_with_different_data_types():
    assert find_all_permutations([['a', 'b'], [1, 2]]) == [['a', 1], [1, 'a'], ['a', 2], [2, 'a'], ['b', 1], [1, 'b'],
                                                           ['b', 2], [2, 'b']]


@pytest.mark.benchmark
def test_large_input(benchmark):
    lists = [[1, 2, 3, 4, 5, 6]] * 12
    benchmark(find_all_permutations, lists)


def test_input_not_a_list_of_lists():
    with pytest.raises(TypeError):
        find_all_permutations([1, 2, 3])


def test_no_duplicates():
    lists = [[1, 2], [3, 4]]
    result = find_all_permutations(lists)
    assert len(result) == len(set(tuple(permutation) for permutation in result))
