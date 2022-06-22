#!/usr/bin/python3
"""SinglyLinkedList class defines and
   Node class defines
"""


class Node:
    """Node of a singly linked list by

       Args:
           data (int): the data of the node
           next_node (Node): the next node
    """

    def __init__(self, data, next_node=None):
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        return (self.__data)

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        return (self.__next_node)

    @next_node.setter
    def next_node(self, value):
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

class SinglyLinkedList:
    """Singly linked class

       Args:
           head (node): the head of the node
    """

    def __init__(self):
        """Initalize a new SinglyLinkedList."""
        self.__head = None

    def sorted_insert(self, value):
        """Insert a new Node to the SinglyLinkedList.
        
        The node is inserted into the list at the correct
        ordered numerical position.
        
        Args:
            value (Node): The new Node to insert.
        """
        new = Node(value)
        if self.__head is None:
            new.next_node = None
            self.__head = new
        elif self.__head.data > new.data:
            new.next_node = self.__head
            self.__head = new
        else:
            tmp = self.__head
            while (tmp.next_node is not None and
                    tmp.next_node.data < new.data):
                tmp = tmp.next_node
            new.next_node = tmp.next_node
            tmp.next_node = new

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        _str = ""
        tmp = self.__head
        while tmp is not None:
            _str += str(tmp.data) + ("\n" if tmp.next_node else "")
            tmp = tmp.next_node
        return (_str)
