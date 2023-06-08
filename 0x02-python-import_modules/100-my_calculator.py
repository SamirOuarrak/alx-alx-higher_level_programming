#!/usr/bin/python3
import sys
from calculator_1 import add, sub, mul, div


def main():
    if len(sys.argv) == 4:
        if sys.argv[2] == "+":
            print(f'{add(int(sys.argv[1]), int(sys.argv[3]))}')
        elif sys.argv[2] == "-":
            print(f'{sub(int(sys.argv[1]), int(sys.argv[3]))}')
        elif sys.argv[2] == "*":
            print(f'{mul(int(sys.argv[1]), int(sys.argv[3]))}')
        elif sys.argv[2] == "/":
            print(f'{div(int(sys.argv[1]), int(sys.argv[3]))}')
    else:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)


if __name__ == "__main__":
    main()
