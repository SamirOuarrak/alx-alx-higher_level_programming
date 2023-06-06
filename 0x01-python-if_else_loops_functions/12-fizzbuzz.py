#!/usr/bin/python3

def fizzbuzz():
    for nb in range(1, 101):
        if abs(nb) % 3 == 0 and abs(nb) % 5 == 0:
            print("FizzBuzz", end=" ")
        elif abs(nb) % 3 == 0:
            print("Fizz", end=" ")
        elif abs(nb) % 5 == 0:
            print("Buzz", end=" ")
        else:
            print("{}".format(nb), end=" ")
