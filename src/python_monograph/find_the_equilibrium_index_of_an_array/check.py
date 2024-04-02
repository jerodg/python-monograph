"""
Python Monograph -> Find the Equilibrium Index of an Array -> Check

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


def equilibrium_index(arr):
    if not isinstance(arr, list):
        raise TypeError('Input must be a list')
    if any(not isinstance(item, int) for item in arr):
        raise ValueError('List must contain only integers')

    n = len(arr)

    # Check for indexes one by one
    # until an equilibrium index is found
    for i in range(n):
        leftsum = 0
        rightsum = 0

        # get left sum
        for j in range(i):
            leftsum += arr[j]

        # get right sum
        for j in range(i + 1, n):
            rightsum += arr[j]

        # if leftsum and rightsum are same,
        # then we are done
        if leftsum == rightsum:
            return i

    # return -1 if no equilibrium index is found
    return -1
