# counting the number of negetive numbers in a 2d matrix

# clarifying question: 0 is not counted as negetive
# array is always square and numbers are sorted

# test matrix

matrix = [
    [-4,-3,-1, 0],
    [-2,-2, 1, 2],
    [-1, 1, 2, 3],
    [ 1, 2, 4, 5]
]

matrix1 = [
    [-2, 0],
    [-1, 0]
]

matrix2 = [[0]]

# negetive number can be identified as condition < 0

# solution that uses O(n**2)
def count_negetive_slow(m):
    count = 0
    for row in m:
        for item in row:
            if item < 0:
                count += 1
    return count

# solution that uses O(n)
def count_negetive_fast(m):
    count = 0
    row_i = 0               # starting at top right corner
    col_i = len(m[0]) - 1
    while col_i >= 0 and row_i < len(m):
        if m[row_i][col_i] < 0:
            count += (col_i + 1)
            row_i += 1
        else:
            col_i -= 1
    return count
    
   
print(count_negetive_slow(matrix))
print(count_negetive_fast(matrix))

print(count_negetive_slow(matrix1))
print(count_negetive_fast(matrix1))

print(count_negetive_slow(matrix2))
print(count_negetive_fast(matrix2))
