#!/usr/bin/env python3
"""Python Monograph: Find Triplets with Zero Sum Solution 03

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


def solution_03(nums: list) -> list[list[int]]:
    """This function finds all unique triplets in the array which gives the sum of zero using a hashing technique.

    Parameters:
        nums (list): The input list of integers.

    Returns:
        list[list[int]]: A list of lists where each list contains three integers that sum up to zero.

    Approach:
    The function creates a hash table for storing the frequency of each element in the array. Then, for each pair of elements,
    it checks if the negative of their sum exists in the hash table. If it does, then it has found a triplet that sums to zero.
    """
    # Create an empty hash table
    freq = {}

    # Add each element to the hash table along with its frequency
    for num in nums:
        if num in freq:
            freq[num] += 1
        else:
            freq[num] = 1

    # Initialize the result list
    result = []

    # For each pair of elements in the array
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            # Calculate the negative of their sum
            sum_neg = -(nums[i] + nums[j])

            # Check if this value exists in the hash table
            if sum_neg in freq:
                # If it does, then you have found a triplet that sums to zero
                triplet = sorted([nums[i], nums[j], sum_neg])

                # Check if the triplet is not already in the result list
                if triplet not in result:
                    result.append(triplet)

    # Return the result list
    return result


if __name__ == '__main__':
    print(__doc__)
