#!/usr/bin/env python3
"""Python Monograph: Test Implementing a Singly Linked List

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
from src.python import LinkedList


def insert_at_beginning_inserts_node_at_beginning():
    linked_list = LinkedList()
    linked_list.insert_at_beginning('data')
    assert linked_list.head.data == 'data'


def insert_at_end_inserts_node_at_end():
    linked_list = LinkedList()
    linked_list.insert_at_end('data')
    assert linked_list.head.data == 'data'


def delete_node_deletes_node_with_given_key():
    linked_list = LinkedList()
    linked_list.insert_at_end('data')
    linked_list.delete_node('data')
    assert linked_list.head == None


def delete_node_does_nothing_if_key_not_found():
    linked_list = LinkedList()
    linked_list.insert_at_end('data')
    linked_list.delete_node('non_existent_data')
    assert linked_list.head.data == 'data'


def print_list_prints_all_node_data():
    linked_list = LinkedList()
    linked_list.insert_at_end('data1')
    linked_list.insert_at_end('data2')
    assert linked_list.print_list() == 'data1 data2 '


def search_returns_true_if_key_found():
    linked_list = LinkedList()
    linked_list.insert_at_end('data')
    assert linked_list.find_substring('data') == True


def search_returns_false_if_key_not_found():
    linked_list = LinkedList()
    linked_list.insert_at_end('data')
    assert linked_list.find_substring('non_existent_data') == False


def test_update_node_when_node_exists():
    linked_list = LinkedList()
    linked_list.insert_at_end('old_value')
    assert linked_list.update('old_value', 'new_value') == True
    assert linked_list.find_substring('new_value') == True


def test_update_node_when_node_does_not_exist():
    linked_list = LinkedList()
    linked_list.insert_at_end('value')
    assert linked_list.update('non_existent_value', 'new_value') == False


def test_sort_on_non_empty_list():
    linked_list = LinkedList()
    linked_list.insert_at_end(3)
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.sort()
    assert linked_list.head.data == 1
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 3


def test_sort_on_empty_list():
    linked_list = LinkedList()
    linked_list.sort()
    assert linked_list.head == None


def test_reverse_on_non_empty_list():
    linked_list = LinkedList()
    linked_list.insert_at_end(1)
    linked_list.insert_at_end(2)
    linked_list.insert_at_end(3)
    linked_list.reverse()
    assert linked_list.head.data == 3
    assert linked_list.head.next.data == 2
    assert linked_list.head.next.next.data == 1


def test_reverse_on_empty_list():
    linked_list = LinkedList()
    linked_list.reverse()
    assert linked_list.head == None


if __name__ == '__main__':
    print(__doc__)
