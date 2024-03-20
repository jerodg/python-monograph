#!/usr/bin/env python3
"""Python Monograph: Merge Two Sorted Lists Solution

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


class ListNode:
    """Definition for a singly-linked list node.

    A singly-linked list node is a data structure that holds a value and a reference to the next node in the list.
    This class is used to create nodes for a singly-linked list.

    Attributes:
        val: The value stored in the node.
        next: The next node in the list.
    """

    def __init__(self, x):
        """
        Initialize a ListNode with a value.

        Args:
            x: The value to be stored in the node.
        """
        self.val = x
        self.next = None


def method_0(l1: ListNode, l2: ListNode) -> ListNode:
    """Merge two sorted linked lists iteratively.

    This function takes two sorted linked lists as input and merges them into a new sorted linked list.
    The new list is made by splicing together the nodes of the first two lists.
    The original lists are not modified.

    Args:
        l1: The first sorted linked list.
        l2: The second sorted linked list.

    Returns:
        A new sorted linked list that contains all the nodes from both input lists.
    """
    dummy = ListNode(0)
    current = dummy

    while l1 and l2:
        if l1.val < l2.val:
            current.next = l1
            l1 = l1.next
        else:
            current.next = l2
            l2 = l2.next
        current = current.next

    current.next = l1 or l2

    return dummy.next


def method_1(l1: ListNode, l2: ListNode) -> ListNode:
    """Merge two sorted linked lists recursively.

    This function takes two sorted linked lists as input and merges them into a new sorted linked list.
    The new list is made by splicing together the nodes of the first two lists.
    The original lists are not modified.
    The function uses recursion to merge the lists.

    Args:
        l1: The first sorted linked list.
        l2: The second sorted linked list.

    Returns:
        A new sorted linked list that contains all the nodes from both input lists.
    """
    if not l1:
        return l2
    elif not l2:
        return l1
    elif l1.val < l2.val:
        l1.next = method_1(l1.next, l2)
        return l1
    else:
        l2.next = method_1(l1, l2.next)
        return l2


def method_2(l1: ListNode, l2: ListNode) -> ListNode:
    """Merge two sorted linked lists using a priority queue.

    This function takes two sorted linked lists as input and merges them into a new sorted linked list.
    The new list is made by splicing together the nodes of the first two lists.
    The original lists are not modified.
    The function uses a priority queue to ensure that the smallest element is always at the front of the queue.

    Args:
        l1: The first sorted linked list.
        l2: The second sorted linked list.

    Returns:
        A new sorted linked list that contains all the nodes from both input lists.
    """
    dummy = ListNode(0)
    current = dummy
    queue = []

    while l1:
        heapq.heappush(queue, (l1.val, l1))
        l1 = l1.next

    while l2:
        heapq.heappush(queue, (l2.val, l2))
        l2 = l2.next

    while queue:
        val, node = heapq.heappop(queue)
        current.next = ListNode(val)
        current = current.next
        node = node.next
        if node:
            heapq.heappush(queue, (node.val, node))

    return dummy.next


if __name__ == '__main__':
    print(__doc__)
