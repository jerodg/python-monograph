#!/usr/bin/env python3
"""Python Monograph: Find Triplets with Zero Sum Solution 00

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


def solution_01(nums: list[int]) -> list[list[int]]:
    """This function finds all unique triplets in the array which gives the sum of zero.

    Parameters:
        nums (list[int]): The input list of integers.

    Returns:
        list[list[int]]: A list of lists where each list contains three integers that sum up to zero.

    Approach:
        The function sorts the input list and then iterates over it. For each number, it uses a two-pointer technique
        to find a pair in the rest of the list that sums up to the negative of the current number, thus ensuring that
        the three numbers sum up to zero. It also handles duplicates by skipping over the same numbers.
    """
    # Sort the input list
    nums.sort()

    # Initialize the result list
    result = []

    # Iterate over the list
    for i in range(len(nums) - 2):
        # Skip over the same numbers to avoid duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        # Initialize the two pointers
        left, right = i + 1, len(nums) - 1

        # Use the two-pointer technique to find a pair that sums up to the negative of the current number
        while left < right:
            total = nums[i] + nums[left] + nums[right]

            # If the total is less than zero, move the left pointer to the right
            if total < 0:
                left += 1

            # If the total is greater than zero, move the right pointer to the left
            elif total > 0:
                right -= 1

            # If the total is zero, add the triplet to the result list
            else:
                result.append([nums[i], nums[left], nums[right]])

                # Skip over the same numbers to avoid duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                # Move both pointers towards the center
                left += 1
                right -= 1

    # Return the result list
    return result


if __name__ == '__main__':
    print(__doc__)
