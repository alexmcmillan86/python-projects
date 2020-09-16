# fibonacci_sequence
# prints the requested number of terms for the fibonacci sequence


# requesting start and end of range from the user
start = int(input('Enter the start number for the range: '))
end = int(input('Enter the end number for the range: '))


def fib_range(start, end):
   n1, n2 = 0, 1
   print("Fibonacci sequence:")
   
   while n1 < end:
      if n1 < start:
         nth = n1 + n2
         n1 = n2
         n2 = nth
         continue
      else:
         print(n1, end=' ')
         nth = n1 + n2
         n1 = n2
         n2 = nth


# function to generate list of fibonacci numbers within range
fib_range(start, end)
    
    
