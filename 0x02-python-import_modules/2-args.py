#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    lst = sys.argv
    lth = len(lst) - 1
    arg = "argument"
    print("{} argument{}{}".format(
            lth,
            "" if lth == 1 else "s",
            "." if lth == 0 else ":"))
    for i in range(1, len(lst)):
        print("{}: {}".format(i, lst[i]))
