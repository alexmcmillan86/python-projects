# finding the second largest value in an array

# cornerstone cases

# empty array -> None
# single value array -> None
# repeating max value [ 2, 2, 1 ] -> 2

arr = [ 1, 3, 4, 5, 0, 2 ]

arr_t1 = []     # test case 1: empty array
arr_t2 = [8]    # test case 2: single value array
arr_t3 = [ 2, 2, 1 ]    # test case 3: duplicate max value


def second_largest(arr):
    if len(arr) == 0 or len(arr) == 1:
        return None
    max_value = max(arr)    # finds the maximum value
    arr.remove(max_value)
    print(max(arr))

    
second_largest(arr_t3)

