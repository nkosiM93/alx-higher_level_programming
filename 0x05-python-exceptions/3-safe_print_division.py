#!/usr/bin/python3

def safe_print_division(a, b):

    answer = None
    try:
        answer = a / b
    except (ZeroDivisionError):
        pass
    finally:
        print("Inside result: {}".format(answer))
        return answer
