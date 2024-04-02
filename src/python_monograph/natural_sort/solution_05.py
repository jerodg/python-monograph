"""
Python Monograph -> Sorting for Humans (Natural Sort) -> Solution 05

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
import re


def natural_sort(lst: list[str]) -> list[str]:
    """
    Sorts a list of strings in a way that is intuitive to humans using a divide and conquer approach.

    This function uses a divide and conquer approach to sort the list of strings. It first divides the list into two halves,
    then recursively sorts each half, and finally merges the two sorted halves into a single sorted list. The sorting is done
    based on the natural order of the strings, which is determined by a helper function `natural_keys`.

    Args:
        lst (List[str]): The list of strings to be sorted.

    Returns:
        List[str]: The sorted list of strings.

    Examples:
        >>> natural_sort(['file1.txt', 'file10.txt', 'file2.txt'])
        ['file1.txt', 'file2.txt', 'file10.txt']

        >>> natural_sort(['image99.png', 'image100.png', 'image101.png', 'image1.png', 'image10.png'])
        ['image1.png', 'image10.png', 'image99.png', 'image100.png', 'image101.png']

        >>> natural_sort(['version1.10', 'version1.2', 'version1.1'])
        ['version1.1', 'version1.2', 'version1.10']
    """

    def natural_keys(s: str) -> list[str | int]:
        """
        Splits a string into a list of parts, each part is either a string of non-digit characters or an integer.

        This helper function is used to determine the natural order of the strings. It splits the input string into parts
        using a regular expression. Each part that consists of digit characters is converted to an integer, and each part
        that consists of non-digit characters is left as a string. The resulting list of parts is used for comparison when
        sorting the strings.

        Args:
            s (str): The string to be split.

        Returns:
            List[Union[str, int]]: The list of parts.
        """
        return [int(part) if part.isdigit() else part for part in re.split(r'(\d+)', s)]

    def merge(left: list[str], right: list[str]) -> list[str]:
        """
        Merges two sorted lists into a single sorted list.

        This helper function is used to merge two sorted lists into a single sorted list. It compares the strings in the
        two lists based on their natural order, which is determined by the `natural_keys` function, and appends the smaller
        string to the merged list. If one list becomes empty before the other, the remaining strings in the non-empty list
        are appended to the merged list.

        Args:
            left (List[str]): The left sorted list.
            right (List[str]): The right sorted list.

        Returns:
            List[str]: The merged sorted list.
        """
        merged, i, j = [], 0, 0
        while i < len(left) and j < len(right):
            if natural_keys(left[i]) < natural_keys(right[j]):
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        while i < len(left):
            merged.append(left[i])
            i += 1
        while j < len(right):
            merged.append(right[j])
            j += 1
        return merged

    # If the list has one or zero elements, it is already sorted
    if len(lst) <= 1:
        return lst

    # Divide the list into two halves
    mid = len(lst) // 2
    left = natural_sort(lst[:mid])
    right = natural_sort(lst[mid:])

    # Merge the two sorted halves into a single sorted list
    return merge(left, right)
