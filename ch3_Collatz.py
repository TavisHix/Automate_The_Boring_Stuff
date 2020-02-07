# The Collatz Sequence
# A function that takes in a integer parameter called num. If the parameter
# is even it will does num // 2 and returns the result. If num is odd
# will do num *2 + 1 and return the result. Program will ask user for a number
# and run collatz until num is equal to 1.

def collatz(num):
    if num % 2 == 0:
        return num // 2
    elif num % 2 == 1:
        return num * 3 + 1


try:
    print("Please enter a number")
    number = int(input())
    while True:
        number = collatz(number)
        print(number)
        if number == 1:
            break
except ValueError:
    print("That's not a valid number")
