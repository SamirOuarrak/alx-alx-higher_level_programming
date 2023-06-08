#!/usr/bin/python3
import sys


def main():
    if len(sys.argv) > 1:
        sum = 0
        for i in range(1, len(sys.argv)):
            sum += int(sys.argv[i])
        print(sum)
    else:
        print(0)


if __name__ == '__main__':
    main()
