#!/usr/bin/env python3
"""Python Monograph: Singly Linked List

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


class Node:
    """
    A class representing a node in a singly linked list.

    Attributes
    ----------
    data : any type
        The data stored in the node.
    next : Node, optional
        The next node in the list, defaults to None.

    Methods
    -------
    __init__(self, data=None)
        Constructs a new Node instance.
    """

    def __init__(self, data=None):
        """
        Constructs a new Node instance.

        Parameters
        ----------
        data : any type, optional
            The data to be stored in the node, defaults to None.
        """
        self.data = data
        self.next = None


class LinkedList:
    """
    A class representing a singly linked list.

    Attributes
    ----------
    head : Node, optional
        The first node in the list, defaults to None.

    Methods
    -------
    __init__(self)
        Constructs a new LinkedList instance.
    insert_at_beginning(self, data)
        Inserts a new node at the beginning of the list.
    insert_at_end(self, data)
        Inserts a new node at the end of the list.
    delete_node(self, key)
        Deletes the first node with the given key from the list.
    print_list(self)
        Prints the data of all nodes in the list.
    search(self, key)
        Searches for a node with the given key in the list.
    update(self, old_value, new_value)
        Updates the first node with the old value to the new value.
    sort(self)
        Sorts the list in ascending order.
    reverse(self)
        Reverses the order of the list.
    """

    def __init__(self):
        """
        Constructs a new LinkedList instance.
        """
        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node at the beginning of the list.

        Parameters
        ----------
        data : any type
            The data to be stored in the new node.
        """
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a new node at the end of the list.

        Parameters
        ----------
        data : any type
            The data to be stored in the new node.
        """
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def delete_node(self, key):
        """
        Deletes the first node with the given key from the list.

        Parameters
        ----------
        key : any type
            The key of the node to be deleted.
        """
        temp = self.head
        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                return
        while temp is not None:
            if temp.data == key:
                break
            prev = temp
            temp = temp.next
        if temp == None:
            return
        prev.next = temp.next
        temp = None

    def print_list(self):
        """
        Prints the data of all nodes in the list.
        """
        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next

    def search(self, key):
        """
        Searches for a node with the given key in the list.

        Parameters
        ----------
        key : any type
            The key of the node to be searched for.

        Returns
        -------
        bool
            True if a node with the key is found, False otherwise.
        """
        current = self.head
        while current:
            if current.data == key:
                return True
            current = current.next
        return False

    def update(self, old_value, new_value):
        """
        Updates the first node with the old value to the new value.

        Parameters
        ----------
        old_value : any type
            The old value to be replaced.
        new_value : any type
            The new value to replace the old value with.

        Returns
        -------
        bool
            True if a node with the old value is found and updated, False otherwise.
        """
        current = self.head
        while current:
            if current.data == old_value:
                current.data = new_value
                return True
            current = current.next
        return False

    def sort(self):
        """
        Sorts the list in ascending order.
        """
        if self.head is None:
            return
        current = self.head
        while current.next:
            next_node = current.next
            while next_node:
                if current.data > next_node.data:
                    current.data, next_node.data = next_node.data, current.data
                next_node = next_node.next
            current = current.next

    def reverse(self):
        """
        Reverses the order of the list.
        """
        prev = None
        current = self.head
        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
        self.head = prev


if __name__ == '__main__':
    print(__doc__)
