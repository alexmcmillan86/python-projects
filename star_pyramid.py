# printing a star pyramid

def pyramid(r):     # input in number of rows to be printed
    for i in range(r):
        print((' '*(r-i-1)) + ('*'*(2*i+1)))
        
pyramid(10)  
    