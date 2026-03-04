#NumberTests.py
#Name: Louis Safranek
#Date: 03-04-2026
#Assignment: Lab 7

from NumberTests import isPrime
"""The isPrime function iterates through all values less than or equal to its input and divides the input by that value.
If the dividend returns as a whole number it appends the divisor to the divisors list.
My thought process for my function here is taking the isPrime of 600851475143 and printing the last value on the list. So even if there are 30 factors of that number it only returns the biggest one. """

def main():
    divisors = isPrime(600851475143)
    print(divisors[-1])
if __name__ == '__main__':
  main()