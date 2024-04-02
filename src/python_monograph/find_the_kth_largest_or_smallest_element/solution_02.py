#!/usr/bin/env python3
"""Python Monograph: Find the kth Largest or Smallest Element Solution 02

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


def partition(nums: list, low: int, high: int) -> int:
    """This function partitions the given list of numbers around a pivot, such that all elements less than or equal to the pivot
    come before the pivot and all elements greater than the pivot come after it. It uses the Lomuto partition scheme,
    where the pivot is always chosen to be the last element in the list.

    Parameters:
        nums (list): The list of numbers to partition.
        low (int): The starting index for the partition.
        high (int): The ending index for the partition.

    Returns:
        int: The index of the pivot after the partition.

    >>> partition([3, 2, 1, 5, 6, 4], 0, 5)
    2
    >>> partition([3, 2, 3, 1, 2, 4, 5, 5, 6], 0, 8)
    2

    The function first chooses the last element in the list as the pivot. It then initializes a variable `i` to `low - 1`. This
    variable keeps track of the boundary between the elements that are less than or equal to the pivot and the elements that are
    greater than the pivot.

    The function then iterates over the list from `low` to `high`. For each element, if the element is less than or equal to the
    pivot, it increments `i` and swaps the element at index `i` with the element at the current index. This ensures that all
    elements less than or equal to the pivot come before all elements greater than the pivot.

    After the iteration, the function swaps the pivot with the element at index `i + 1`. This places the pivot in its final
    sorted position in the list.

    The function then returns the index of the pivot.
    """
    pivot = nums[high]
    i = low - 1

    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]

    nums[i + 1], nums[high] = nums[high], nums[i + 1]

    return i + 1


def quickselect(nums: list, k: int, low: int, high: int) -> int:
    """This function implements the QuickSelect algorithm, which is an efficient in-place variation of the QuickSort algorithm.
    It is used to find the kth smallest or largest element in an unordered list.

    Parameters:
        nums (list): The list of numbers to search.
        k (int): The index of the element to find.
        low (int): The starting index for the search.
        high (int): The ending index for the search.

    Returns:
        int: The kth smallest or largest element in the list.

    >>> quickselect([3, 2, 1, 5, 6, 4], 2, 0, 5)
    2
    >>> quickselect([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 0, 8)
    3

    The function first checks if the list contains only one element. If so, it returns that element.

    The function then partitions the list around a pivot using the `partition` function. The pivot is chosen such that all
    elements less than or equal to the pivot come before the pivot and all elements greater than the pivot come after it.

    If the index of the pivot is equal to `k`, the function returns the pivot. If `k` is less than the index of the pivot,
    the function recursively searches the left part of the list. If `k` is greater than the index of the pivot, the function
    recursively searches the right part of the list.
    """
    if low == high:
        return nums[low]

    pivot_index = partition(nums, low, high)

    if k == pivot_index:
        return nums[k]
    elif k < pivot_index:
        return quickselect(nums, k, low, pivot_index - 1)
    else:
        return quickselect(nums, k, pivot_index + 1, high)


def solution_02(nums: list, k: int, largest: bool = True) -> int:
    """Finds the kth largest or smallest element in a list using the QuickSelect algorithm.

    This function uses the QuickSelect algorithm to find the kth largest or smallest element in a list. The QuickSelect algorithm
    is an efficient in-place variation of the QuickSort algorithm.

    Args:
        nums (list): The list of numbers to search.
        k (int): The index of the element to find.
        largest (bool, optional): A flag indicating whether to find the kth largest or smallest element. Defaults to True.

    Returns:
        int: The kth largest or smallest element in the list.

    Examples:
        >>> solution_02([3, 2, 1, 5, 6, 4], 2)
        5
        >>> solution_02([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, False)
        3

    If `largest` is True, the function finds the kth largest element. It does this by subtracting `k` from the length of the list
    and passing the result as the second argument to the `quickselect` function.

    If `largest` is False, the function finds the kth smallest element. It does this by subtracting 1 from `k` and passing the
    result as the second argument to the `quickselect` function.
    """
    if k > len(nums):
        raise IndexError('k cannot be larger than the list length.')

    if largest:
        return quickselect(nums, len(nums) - k, 0, len(nums) - 1)
    else:
        return quickselect(nums, k - 1, 0, len(nums) - 1)


if __name__ == '__main__':
    print(__doc__)
