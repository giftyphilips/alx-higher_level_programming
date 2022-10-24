#!/usr/bin/python3
# 1-my_list.py
""" Defines a new class """


class MyList(list):
    """ Mylist class that inherist from list """

    def print_sorted(self):
        """ Fucntion that prints a sorted list """
        print(sorted(self))
