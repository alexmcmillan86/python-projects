# prime_nums_in_range script:
# generates a list of prime numbers within a user specified range

def prime_nums(a, b):
    prime_list = []
    
    for n in range(a, b):
        if n > 1:
            for i in range(2, n):
                if (n % i) == 0:
                    break
            else:
                prime_list.append(n)
   
    print(prime_list)


# requesting start and end of range from the user
start = int(input('Enter the start number for the range: '))
end = int(input('Enter the end number for the range: '))

# function to generate list of prime numbers within range
prime_nums(start, end)