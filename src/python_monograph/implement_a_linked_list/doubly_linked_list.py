#!/usr/bin/env python3
"""Python Monograph: Doubly Linked List

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
    A class to represent a node in a doubly linked list.

    ...

    Attributes
    ----------
    data : any
        the data to be stored in the node
    next : Node, optional
        reference to the next node in the doubly linked list, defaults to None
    prev : Node, optional
        reference to the previous node in the doubly linked list, defaults to None

    Methods
    -------
    __init__(self, data=None)
        Constructs a Node with the specified data and next and prev set to None.
    """

    def __init__(self, data=None):
        """
        Constructs a Node with the specified data and next and prev set to None.

        Parameters
        ----------
        data : any
            The data to be stored in the node. Defaults to None.
        """

        self.data = data
        self.next = None
        self.prev = None


class DoublyLinkedList:
    """
    A class to represent a doubly linked list.

    ...

    Attributes
    ----------
    head : Node, optional
        the start of the doubly linked list, defaults to None

    Methods
    -------
    __init__(self)
        Constructs a DoublyLinkedList with the head set to None.
    insert_at_beginning(self, data)
        Inserts a new node at the beginning of the list.
    insert_at_end(self, data)
        Inserts a new node at the end of the list.
    delete_node(self, key)
        Deletes a node with the specified key from the list.
    search(self, key)
        Searches for a node with the specified key in the list.
    update(self, old_value, new_value)
        Updates the value of a node in the list.
    sort(self)
        Sorts the nodes in the list in ascending order.
    reverse(self)
        Reverses the order of the nodes in the list.
    print_list(self)
        Prints the data of all nodes in the list.
    """

    def __init__(self):
        """
        Constructs a DoublyLinkedList with the head set to None.
        """

        self.head = None

    def insert_at_beginning(self, data):
        """
        Inserts a new node at the beginning of the list.

        Parameters
        ----------
        data : any
            The data to be stored in the new node.
        """

        new_node = Node(data)
        new_node.next = self.head
        if self.head is not None:
            self.head.prev = new_node
        self.head = new_node

    def insert_at_end(self, data):
        """
        Inserts a new node at the end of the list.

        Parameters
        ----------
        data : any
            The data to be stored in the new node.
        """

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            last_node = self.head
            while last_node.next:
                last_node = last_node.next
            last_node.next = new_node
            new_node.prev = last_node

    def delete_node(self, key):
        """
        Deletes a node with the specified key from the list.

        Parameters
        ----------
        key : any
            The key of the node to be deleted.
        """

        temp = self.head
        while temp is not None:
            if temp.data == key:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if temp == self.head:
                    self.head = temp.next
                temp = None
                return
            temp = temp.next

    def search(self, key):
        """
        Searches for a node with the specified key in the list.

        Parameters
        ----------
        key : any
            The key of the node to be searched for.

        Returns
        -------
        bool
            True if a node with the specified key is found, False otherwise.
        """

        temp = self.head
        while temp:
            if temp.data == key:
                return True
            temp = temp.next
        return False

    def update(self, old_value, new_value):
        """
        Updates the value of a node in the list.

        Parameters
        ----------
        old_value : any
            The old value to be replaced.
        new_value : any
            The new value to replace the old value.

        Returns
        -------
        bool
            True if a node with the old value is found and updated, False otherwise.
        """

        temp = self.head
        while temp:
            if temp.data == old_value:
                temp.data = new_value
                return True
            temp = temp.next
        return False

    def sort(self):
        """
        Sorts the nodes in the list in ascending order.
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
        Reverses the order of the nodes in the list.
        """

        temp = None
        current = self.head
        while current:
            temp = current.prev
            current.prev = current.next
            current.next = temp
            current = current.prev
        if temp:
            self.head = temp.prev

    def print_list(self):
        """
        Prints the data of all nodes in the list.
        """

        temp = self.head
        while temp:
            print(temp.data, end=' ')
            temp = temp.next


if __name__ == '__main__':
    print(__doc__)
