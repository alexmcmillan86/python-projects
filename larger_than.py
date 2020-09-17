# comparing two strings representing integers to check which value is larger


# Clarifying questions
# solve without using int(str) function
# if numbers are the same -> False
# no negetive numbers to consider

def larger_than(num1, num2):
    if len(num1) > len(num2):
        print('True')
        return True
    elif len(num1) < len(num2):
        print('False')
        return False

    # numbers must have same number of digits
    for i in range(len(num1)):
        if num1[i] > num2[i]:
            print('True!')
            return True
        elif num1[i] < num2[i]:
            print('False')
            return False
        else:
            if i == (len(num1) - 1):
                print('False')
                return False
            continue
    
    
larger_than('12521', '1241')



