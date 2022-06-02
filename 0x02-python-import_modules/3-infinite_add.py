#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    lst = sys.argv
    for i in range(1, len(lst)):
        sum = sum + int(lst[i])
    print(sum)
