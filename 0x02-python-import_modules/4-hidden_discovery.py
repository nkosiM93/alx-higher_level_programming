#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    if len(dir(hidden_4)) == 0:
        exit()
    for name in dir(hidden_4):
        if name[0] == '_':
            continue
        print(name)
