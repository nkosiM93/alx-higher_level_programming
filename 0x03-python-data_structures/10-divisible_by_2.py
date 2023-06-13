#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    if (len(my_list) == 0):
        return []

    new_lst = []

    for i in my_list:
        if i % 2 == 0:
            new_lst.append(True)
        else:
            new_lst.append(False)

    return new_lst
# Below is a smarter option, more redeable
# my_list.sort()
# return(my_list[-1])
