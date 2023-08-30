#!/usr/bin/python3

def safe_print_list(my_list=[], x=0):
    count = 0

    try:
        for i, j in enumerate(my_list):
            if i < x:
                count += 1
                print(j, end="")
            else:
                print()
                return count
    except IndexError:
        pass
    print()
    return count
