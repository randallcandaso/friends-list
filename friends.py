'''

File: friends.py
Author: Randall Candaso
Course/Section: CSC 120-002
Purpose: This program takes an inputted file and reads
in the names in the file. Each name is used to create
a node that is then inserted into a linked list. In
addition, each name node will have a friends attribute
that, itself, links to another linked list containing
that name's friends. The user will input two names
into the program and the list of name(s) in common
will be returned.

'''

from linked_list import LinkedList
from linked_list import Node

def main():
    read = input('Input file: ')
    file = open(read, 'r')
    name1 = input('Name 1: ')
    name2 = input('Name 2: ')
    ll, check = addition(file)
    unknown(name1, name2, check, ll)

def unknown(name1, name2, list, ll):
    '''

    Takes the two names inputted and identifies
    whether the names are in the file.

    :param name1: first name inputted
    :param name2: second name inputted
    :param list: list of names in the linked
    list
    :param ll: the linked list containing all
    the names and linked friends
    :return: If an inputted name is not in the
    file, an error is returned, else the names
    and the linked list enter another function
    '''
    empty = [name1, name2]
    organ = sorted(empty)
    if organ[0] not in list:
        print('ERROR: Unknown person ' + organ[0])
    elif organ[1] not in list:
        print('ERROR: Unknown person ' + organ[1])
    else:
        return common(name1, name2, ll)

def addition(file):
    '''

    The inputted file is read in and the names inside
    are created into nodes, which are then entered
    into a linked list. If applicable, a node will
    contain an attribute that refers to a linked
    list of nodes of the friends that the original
    node has.

    :param file: the inputted file by the user
    :return: a linked list containing each name
    node and their list of friends
    '''
    base = LinkedList()
    check = []
    for i in file.readlines():
        temporary = i.split()
        for j in range(len(temporary)):
            if j == 0:
                new = temporary[j]
                if new not in check:
                    node = Node(new)
                    initial = Node(temporary[j + 1])
                    node._friend.add(initial)
                    base.add(node)
                    check.append(new)
                else:
                    node = base.find(new)
                    initial = Node(temporary[j + 1])
                    node._friend.add(initial)
            else:
                new = temporary[j].strip('\n')
                if new not in check:
                    node = Node(new)
                    initial = Node(temporary[j - 1])
                    node._friend.add(initial)
                    base.add(node)
                    check.append(new)
                else:
                    node = base.find(new)
                    initial = Node(temporary[j - 1])
                    node._friend.add(initial)
    return base, check

def common(name1, name2, ll):
    '''

    Based off the linked list, the function
    reads in the list of friends for both
    names and determines if they have any
    in common.

    :param name1: first name inputted
    :param name2: second name inputted
    :param ll: linked list containing all
    the name nodes and their list of friends
    :return: the list of friend(s) in common
    of both inputted names
    '''
    node_1 = ll.find(name1)
    node_2 = ll.find(name2)
    list_1 = node_1.friends()
    list_2 = node_2.friends()
    empty = []
    for i in list_1:
        if i in list_2:
            empty.append(i)
    new = sorted(empty)
    if len(new) != 0:
        print('Friends in common:')
        for j in new:
            print(j)

main()