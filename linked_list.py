'''

File: linked_list.py
Author: Randall Candaso
Course/Section: CSC 120-002
Purpose: For the creation of both nodes
and linked lists, in external file use.

'''

class LinkedList:
    '''

    Creates a linked list class
    that links one node to another
    and so on.

    '''
    def __init__(self):
        '''

        Constructs the head of the
        list

        '''
        self._head = None

    def add(self, node):
        '''

        Adds an inputted node to
        the front of the list

        :param node: a pre-existing
        node
        :source: CloudCoder
        '''
        node._next = self._head
        self._head = node

    def remove(self):
        '''

        Removes the head node
        of the linked list

        :return: the removed node
        :source: CloudCoder
        '''
        assert self._head != None
        _node = self._head
        self._head = _node._next
        _node._next = None
        return _node

    def insert(self, node1, node2):
        '''

        Puts node 2 after node 1

        :param node1: the node
        that will be first
        :param node2: the node
        that proceeds the first
        :source: CloudCoder
        '''
        assert node1 != None
        node2._next = node1._next
        node1._next = node2

    def find(self, word):
        '''

        Finds the node that contains
        the inputted word attribute

        :param word: an inputted word
        :return: the node that
        contains the matching word
        attribute
        '''
        current = self._head
        while current != None:
            if current._name == word:
                return current
            current = current._next

    def __str__(self):
        '''

        Returns a formal string for
        the linked list

        :source: CloudCoder
        '''
        string = 'List[ '
        curr_node = self._head
        while curr_node != None:
            string += str(curr_node)
            curr_node = curr_node.next()
        string += ']'
        return string

class Node:
    '''

    Constructs a node around an
    inputted name

    '''
    def __init__(self, name):
        '''

        Initializes a name attribute and
        a next attribute.
        Also creates a friend attribute
        that refers to a linked list.

        :param name:
        '''
        self._name = name
        self._friend = LinkedList()
        self._next = None

    def friends(self):
        '''

        Iterates through the friends attribute
        which refers to a linked list. Each node
        name in the list is then appended into
        'empty'

        :return: the list of node names
        '''
        empty = []
        current = self._friend._head
        while current != None:
            empty.append(current._name)
            current = current._next
        return empty

    def name(self):
        '''

        Returns the name attribute of the
        node

        '''
        return self._name

    def next(self):
        '''

        Returns the next attribute of the
        node

        '''
        return self._next

    def __str__(self):
        '''

        Returns a formal string representation
        of the node

        '''
        return str(self._name) + "; "