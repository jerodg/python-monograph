"""
Python Monograph: Calculate Product Sum of a Nested Array Solution 00

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


def calculate_product_sum(arr: list[int | list], depth: int = 1) -> int:
    """
    Calculates the product sum of a nested array using a recursive method.

    The product sum of an array is defined as the sum of its elements multiplied by their respective depths. If an
    element is a list, its product sum is calculated recursively by multiplying the sum of its elements with its
    depth plus one.

    Args:
        arr (list[int | list]): A list that can contain integers or other nested lists.
        depth (int, optional): The initial depth of the array. Defaults to 1.

    Returns:
        int: The product sum of the array.

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
    # Initialize the total sum
    total_sum = 0

    # Iterate over the elements in the array
    for ele in arr:
        # If the element is a list, recursively calculate its product sum and add it to the total sum
        # If the element is an integer, multiply it by the depth and add it to the total sum
        total_sum += calculate_product_sum(ele, depth + 1) if isinstance(ele, list) else ele * depth

    # Return the total sum
    return total_sum
