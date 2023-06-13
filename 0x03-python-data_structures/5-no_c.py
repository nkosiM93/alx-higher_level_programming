#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        return [char for char in my_string 
                if char != 'C' or char != 'c']
