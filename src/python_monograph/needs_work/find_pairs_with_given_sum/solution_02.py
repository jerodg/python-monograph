#!/usr/bin/env python3
"""Python Monograph: Find Pairs With the Given Sum Solution 02

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


def solution_02(arr: List[int], req_sum: int) -> Tuple[int, List[Tuple[int, int]]]:
    """
    This function returns the number of pairs in the input list `arr` that sum up to `req_sum` using a two-pointer approach,
    and a list of the pairs.

    The function uses a two-pointer approach. It first sorts the array, then initializes two pointers, one at the start
    of the array and one at the end. It then iterates over the array, and for each iteration, it calculates the sum of
    the elements at the two pointer positions. If the sum is equal to the target sum, it increments the count, adds the pair to
    the list, and moves
    both pointers towards the center of the array. If the sum is less than the target sum, it moves the start pointer
    towards the end of the array. If the sum is greater than the target sum, it moves the end pointer towards the start
    of the array.

    Args:
        arr (List[int]): A list of integers.
        req_sum (int): The required sum.

    Returns:
        Tuple[int, List[Tuple[int, int]]]: The number of pairs in `arr` that sum up to `req_sum`, and a list of the pairs.

    Doctests:
    >>> solution_02([1, 5, 7, 1], 6)
    (2, [(1, 5), (5, 1)])
    >>> solution_02([1, 1, 1, 1, 1, 1, 1, 1], 2)
    (28, [(1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1),
    (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1), (1, 1)])
    >>> solution_02([1, 7, 6, 2, 5, 4, 3, 1, 9, 8], 7)
    (4, [(1, 6), (6, 1), (2, 5), (5, 2)])
    """
    arr.sort()  # Sort the array
    left = 0  # Initialize the left pointer at the start of the array
    right = len(arr) - 1  # Initialize the right pointer at the end of the array
    count = 0  # Initialize count to 0
    pairs = []  # Initialize pairs to an empty list
    while left < right:  # While the left pointer is less than the right pointer
        current_sum = arr[left] + arr[right]  # Calculate the sum of the elements at the two pointer positions
        if current_sum == req_sum:  # If the sum is equal to the target sum
            count += 1  # Increment the count
            pairs.append((arr[left], arr[right]))  # Add the pair to the list
            left += 1  # Move the left pointer towards the center of the array
            right -= 1  # Move the right pointer towards the center of the array
        elif current_sum < req_sum:  # If the sum is less than the target sum
            left += 1  # Move the left pointer towards the end of the array
        else:  # If the sum is greater than the target sum
            right -= 1  # Move the right pointer towards the start of the array
    return count, pairs  # Return the count and the list of pairs


if __name__ == '__main__':
    print(__doc__)
