#!/usr/bin/python3

def no_c(my_string):
    if my_string:
        for i, char in enumerate(my_string):
            if char == 'C' or char == 'c':
                my_string[i] = []
