#!/usr/bin/python3

def uppercase(str):
    for i in range(0, len(str)):
        print('{}'.format(' ' if ord(str[i]) == 32 else 
            str[i] if ord(str[i])>= 48 and ord(str[i])<= 57 else 
            chr(ord(str[i]) - 32)), end='')
    print()
