#!/usr/bin/python3

def safe_print_list_integers(my_list=[], x=0):
    
    count = 0
    for i, j in enumerate(my_list):
        if i < x:
            try:
                print("{:d}".format(j), end="")
                count =+ 1
            except (ValueError):
                pass
            except (IndexError):
                raise
    print()
    return count
