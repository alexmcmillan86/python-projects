# a function to implement bubble sort


x = [ 3, 5, 6, 35, 18, 32, 45, 7 ]

def bubble_sort(x):
    l = len(x) - 1
    for i in range(l):
        for j in range(l-i):
            if x[j] > x[j+1]:
                x[j],x[j+1] = x[j+1],x[j]
    return x

print(bubble_sort(x))
    

