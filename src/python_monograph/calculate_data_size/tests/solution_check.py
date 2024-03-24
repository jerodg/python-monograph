"""
Python Monograph -> Calculate Data Size -> Solution Check

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
# This is a test file to check the correctness of the solution for the problem of calculating the data size of a
# nested array. It compares the output of the solution with the expected output for different test cases.

import ast


# def calculate_product_sum(arr: list[int | list]) -> int:
#     """
#     Calculates the total data size of a nested array using ast.literal_eval()
#
#     This function takes a nested list as input and returns the total data size. The data size of an array is defined
#     as the sum of its elements. If an element is a list, its data size is calculated recursively by summing the sizes
#     of its elements.
#
#     Args:
#         arr (list[int | list]): A list that can contain integers or other nested lists.
#
#     Returns:
#         int: The total data size of the array.
#
#     Examples:
#         >>> calculate_product_sum([1, 2, 3])
#         6
#         >>> calculate_product_sum([1, 2, [3, 4]])
#         10
#         >>> calculate_product_sum([1, [2, [3, [4, [5]]]]])
#         15
#         >>> calculate_product_sum([1, 2, 3, 4, 5])
#         15
#         >>> calculate_product_sum([[1,2,3],[4,[5,6]],7])
#         28
#     """
#     return sum(ast.literal_eval(str(arr).replace('[', '').replace(']', '')))


def calculate_product_sum(array, multiplier=1):
    """

    Args:
        array ():
        multiplier ():

    Returns:

    Examples:
        >>> calculate_product_sum([5, 2, [7, -1], 3, [6, [-13, 8], 4]])
        27
        >>> calculate_product_sum([1, [2, [3, [4, [5]]]]])
        105
        >>> calculate_product_sum([1, 2, 3, 4, 5])
        15
        >>> calculate_product_sum([[1, 2], [3, 4], [5, 6]])
        42
        >>> calculate_product_sum([1, [2, 3, [4, 5], 6, 7], 8])
        102
    """
    total_sum = 0
    for element in array:
        if isinstance(element, list):
            total_sum += calculate_product_sum(element, multiplier + 1) * multiplier
        else:
            total_sum += element * multiplier

    return total_sum
