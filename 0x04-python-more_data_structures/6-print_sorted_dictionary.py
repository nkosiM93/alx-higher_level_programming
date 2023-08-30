#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    if a_dictionary:
        sorted_list = {k: a_dictionary[k] for k in sorted(a_dictionary)}

        for i, j in sorted_list.items():
            print(str(i) + ": " + str(j))
    else:
        print()
