#!/usr/bin/python3

for i in range(100):
    if i < 99:
        print("{}".format("0" if i < 10 else "") + f"{i}" + ",", end=" ")
    else:
        print(i)
