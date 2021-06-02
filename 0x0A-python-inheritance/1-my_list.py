#!/usr/bin/python3
'''A class MyList that inherits from list: '''


class MyList(list):
    '''A class that inherited the method of list object'''
    def print_sorted(self):
        '''This method print the values sorted'''
        new_list = sorted(self)
        print(new_list)
