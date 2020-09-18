# finding a pair of numbers in a list that sum to a target

# test data
target = 10
numbers = [ 3, 4, 1, 2, 9 ]

# test solution -> 1, 9 can be summed to make 10

# additional test data
numbers1 = [ -11, -20, 2, 4, 30 ]
numbers2 = [ 1, 2, 9, 8 ]
numbers3 = [ 1, 1, 1, 2, 3, 4, 5 ]

# function with O(n)
def sum_target(nums, target):
    seen = {}
    for num in nums:
        remaining = target - num
        if remaining in seen:
            return num, remaining
        else:
           seen[num] = 1 
    return 'No pairs that sum to target'
   
    
print(sum_target(numbers, target))
print(sum_target(numbers1, target))
print(sum_target(numbers2, target))
print(sum_target(numbers3, target))

