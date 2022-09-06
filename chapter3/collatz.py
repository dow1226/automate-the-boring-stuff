"""
The function has one parameter named number.
If number is even, then collatz() should print number // 2 and return this value.
If number is odd, then collatz() should print and return 3 * number + 1.
Then write a program that lets the user type in an integer and that
keeps calling collatz() on that number until the function returns the value 1.
"""


def collatz(number):
    if number % 2 == 0:
        number = number // 2
        print(number)
        return number
    else:
        number = 3 * number + 1
        print(number)
        return number


def run():
    try:
        number = int(input('Enter a number: '))
        result = collatz(number)
        while result != 1:
            result = collatz(result)
    except ValueError:
        print('Invalid value entered')


if __name__ == '__main__':
    run()
