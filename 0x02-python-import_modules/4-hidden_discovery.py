#!/usr/bin/python3

if __name__ == "__main__":
    from hidden_4 import *

    all = dir()
    for i in range(0, len(all)):
        if all[i][:2] != "__":
            print("{}".format(all[i]))
