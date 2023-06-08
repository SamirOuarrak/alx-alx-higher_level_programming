#!/usr/bin/python3

import sys


def main():
    if len(sys.argv) == 1:
        print("0 arguments.")
    else:
        print(f"{int(len(sys.argv)) - 1} argument", end="")
        if len(sys.argv) > 2:
            print("s", end="")
        print(":")
        for i in range(1, len(sys.argv)):
            print(f"{int(i)}: {str(sys.argv[i])}")


if __name__ == "__main__":
    main()
