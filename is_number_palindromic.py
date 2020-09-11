import math


def is_palindrome_number(x: int) -> bool:
    if x <= 0:
        print("Enter a number greater than 0!")
        return False

    num_digits = math.floor(math.log10(x)) + 1
    mask = 10 ** (num_digits - 1)
    for i in range(num_digits // 2):
        if x // mask != x % 10:
            print("Number is not palindromic!")
            return False
        x %= mask
        x //= 10
        mask //= 100
    print("Number is palindromic")
    return True


# ask user for a number input
number = int(input("Enter a number: "))
is_palindrome_number(number)
