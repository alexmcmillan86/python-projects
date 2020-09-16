# fibonacci_sequence
# prints the requested number of terms for the fibonacci sequence


nterms = int(input("How many terms? "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if nterms <= 0:
   print("Please enter a positive integer!")
else:
   print("Fibonacci sequence:")
   while count < nterms:
       print(n1, end=' ')
       nth = n1 + n2
       n1 = n2
       n2 = nth
       count += 1   
    
    