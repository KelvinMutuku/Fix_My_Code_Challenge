#!/usr/bin/python3
""" FizzBuzz
    Change of logic if (k % 3) == 0 and (k % 5) == 0:
"""
import sys


def fizzbuzz(a):
    """
    FizzBuzz function prints numbers from 1 to n separated by a space.
    
    - For multiples of three print "Fizz" instead of the number and for
      multiples of five print "Buzz".
    - For numbers which are multiples of both three and five print "FizzBuzz".
    """
    if a < 1:
        return

    tmp_result = []
    for k in range(1, a + 1):
        if (k % 3) == 0 and (k % 5) == 0:
            tmp_result.append("FizzBuzz")
        elif (k % 3) == 0:
            tmp_result.append("Fizz")
        elif (k % 5) == 0:
            tmp_result.append("Buzz")
        else:
            tmp_result.append(str(i))
    print(" ".join(tmp_result))


if __name__ == '__main__':
    if len(sys.argv) <= 1:
        print("Missing number")
        print("Usage: ./0-fizzbuzz.py <number>")
        print("Example: ./0-fizzbuzz.py 89")
        sys.exit(1)

    number = int(sys.argv[1])
    fizzbuzz(number)
