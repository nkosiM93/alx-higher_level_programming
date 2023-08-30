#!/usr/bin/python3

def list_division(my_list_1, my_list_2, list_length):

    answers = []
    try:
        for i in range(list_length):
            try:
                answers.append(my_list_1[i] / my_list_2[i])
            except TypeError:
                print("wrong type")
                answers.append(0)
            except ZeroDivisionError:
                answers.append(0)
                print("division by 0")
            except IndexError:
                answers.append(0)
                print("out of range")
    except ValueError:
        print("out of range")
    finally:
        return answers
