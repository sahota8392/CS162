# Author: Harpreet Sahota
# GitHub: sahota8392
# Date: 7/29/2023
# Description: LinkedList class with recursive implementations


class Node:
    """
    Represents node in the linked list
    """

    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    """
    Recursive implementation for - add, remove, contains, insert, reverse
    The reverse method does not change data value each node holds
    Reverse rearranges order of nodes in linked list
    """

    def __init__(self):
        self._head = None

    def get_head(self):
        """returns head"""
        return self._head

    def add(self, val, current=None):
        """Adds node containing val to end of linked list"""

        def add_helper(val, current):
            """add helper"""
            if current is None:
                return Node(val)

            current.next = add_helper(val, current.next)
            return current

        self._head = add_helper(val, self._head)

    def remove(self, val):
        """Removes node containing val from linked list"""

        def remove_helper(current, val, previous=None):
            """remove helper"""
            if current is None:
                return current

            if current.data == val:
                if previous is None:
                    self._head = current.next
                else:
                    previous.next = current.next
                return current.next
            else:
                current.next = remove_helper(current.next, val, current)
                return current

        self._head = remove_helper(self._head, val)

    def contains(self, key):
        """Return true if list has Node with value key, else False"""

        def contains_helper(current):
            """helper for contains method"""
            if current is None:
                return False

            if current is not None and current.data == key:
                return True
            return contains_helper(current.next)

        return contains_helper(self._head)

    def insert(self, val, pos):
        """Inserts a node containing val into the linked list at position pos"""
        if self._head is None:
            self.add(val)
            return

        if pos == 0:
            temp = self._head
            self._head = Node(val)
            self._head.next = temp
        else:
            self.insert_helper(self._head, val, pos)

    def insert_helper(self, current, val, pos):
        """helper for insert"""
        if current.next is None:
            current.next = Node(val)
            return

        if pos == 1:
            temp = current.next
            current.next = Node(val)
            current.next.next = temp
            return

        self.insert_helper(current.next, val, pos-1)

    #
    def reverse(self):
        """"Reverses the linked list"""

        def reverse_helper(current, previous):
            """helper for reverse method"""
            if current is None:
                self._head = previous
                return

            following = current.next
            current.next = previous
            reverse_helper(following, current)

        reverse_helper(self._head, None)

    def to_plain_list(self):
        """
        Returns a regular Python list containing the same values,
        in the same order, as the linked list
        """

        def to_plain_list_helper(current, result=None):
            if current is None:
                return result

            if result is None:
                result = []

            result.append(current.data)
            return to_plain_list_helper(current.next, result)

        return to_plain_list_helper(self._head)

    def rec_display(self, a_node):
        """recursive display method"""
        if a_node is None:
            return
        print(a_node.data, end=" ")
        self.rec_display(a_node.next)

    def display(self):
        """recursive display helper method"""
        self.rec_display(self._head)
