#NumberTests.py
#Name: Louis Safranek
#Date: 03-04-2026
#Assignment: Lab 7

def isThreeOrFive(n):
  """Returns boolean determination if number is multiple of 3 or 5"""

  if n % 3 == 0 or n % 5 == 0:
    return True
  else:
    return False

def isPrime(p):
  """Returns boolean (True/False) if the value given is prime."""
  divisors = []
  divisor = 2
  while divisor <= p**0.5:
    if p % divisor == 0:
      if divisor != 1 and divisor != p:
        divisors.append(divisor)
    divisor += 1
  return divisors

def isEven(n):
  """Returns boolean about given value being even."""

  if n % 2 == 0:
    return True
  else:
    return False

def addNum(numList, num):
  """Adds the given number to the given list. Does not add duplicate values."""

  numList.append(num)


def fibonacciSequence(value):
  """Returns a list of numbers in the fibonacci sequence up to the given value"""

  nums = [1, 2]
  size = 2
  n = nums[size - 1] + nums[size - 2]

  while n < value:
    addNum(nums, n)
    size = len(nums)
    n = nums[size - 1] + nums[size - 2]

  return nums
def isDivisibleUpto20(num):
  """returns True if num is evenly divisible by all numbers 1-20"""
  for i in range (1,21):
    if num % i != 0:
      return False
  return True

#Test your new functions in this main
def main():
  knownPrimes = [3, 7, 11, 13, 17]

  num = int(input("Enter a number: "))

  if isPrime(num):
    print("%d is a prime number" %(num))

  if isEven(num):
    print("%d is an even number" %(num))


if __name__ == '__main__':
    main()
