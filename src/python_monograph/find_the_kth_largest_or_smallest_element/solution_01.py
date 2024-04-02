#!/usr/bin/env python3
"""Python Monograph: Find the kth Largest or Smallest Element Solution 01

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
import heapq


def solution_01(nums: list, k: int, largest: bool = True) -> int:
    """This function finds the kth largest or smallest element in a given list of numbers using a heap.

    Parameters:
        nums (list): A list of integers. This is the list in which the function will search for the kth largest or smallest element.
        k (int): An integer that represents the position of the element to find.
        largest (bool): A boolean that indicates whether to find the kth largest or smallest element. It defaults to True,
            which means the function will find the kth largest element by default.

    Returns:
        int: The kth largest or smallest element in the list.

    The function uses a heap to keep track of the k largest or smallest elements seen so far. It iterates over the list,
    pushing each element onto the heap. If the size of the heap exceeds k, it pops the smallest element off the heap. This
    ensures that the heap always contains the k largest elements seen so far. At the end of the function, the smallest element on
    the heap is the kth largest element in the list.

    If the `largest` parameter is set to False, the function negates each element before pushing it onto the heap and after
    popping it off. This effectively turns the min-heap into a max-heap, allowing it to keep track of the k smallest elements
    instead of the k largest elements.

    >>> solution_01([3, 2, 1, 5, 6, 4], 2)
    5
    >>> solution_01([3, 2, 1, 5, 6, 4], 2, largest=False)
    2
    >>> solution_01([3, 2, 3, 1, 2, 4, 5, 5, 6], 4)
    4
    """
    if k <= 0:
        raise IndexError('k cannot be zero or negative.')

    if k > len(nums):
        raise IndexError('k cannot be larger than the list length.')

    heap = []
    for num in nums:
        if not largest:
            num = -num
        heapq.heappush(heap, num)

        if len(heap) > k:
            heapq.heappop(heap)

    if largest:
        return heapq.heappop(heap)
    else:
        return abs(heapq.heappop(heap))


if __name__ == '__main__':
    print(__doc__)
