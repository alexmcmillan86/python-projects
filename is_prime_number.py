# is_prime_number script:


def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if (n % i) == 0:
                print(f'{num} is not a prime number.')
                break
        else:
            print(f'{num} is a prime number!')
    else:
        print(f'{num} is not a prime number')

# requesting a number from the user
num = int(input('Enter a whole number: '))

# function to check if number is prime
is_prime(num)