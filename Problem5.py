from NumberTests import isDivisibleUpto20

"""The isDivisibleUpto20 function checks to see if the input num is divisible by every num 1-20.
In this problem I am taking the divisible by 20 function and passing numbers into it till it returns true otherwise it increments to the next number up"""
def main():
    num = 1
    while True:
        if isDivisibleUpto20(num) is True:
            print("The lowest number evenly divisible by numbers 1-20 is", num)
            return
        else:
            num += 1

if __name__ == '__main__':
  main()
