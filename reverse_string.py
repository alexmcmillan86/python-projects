# reverse string

# test case: string cannot be empty and is same length

# test case 1: "ABC" and "CBA" -> True

def is_reverse(str1, str2):
    for i in range(len(str1)):
        i_2 = len(str2) - i - 1
        if str1[i] != str2[i_2]:
            print('False')
            return False
    print('True')
    return True
    


string1 = 'ABC'
string2 = 'CBD'
    
is_reverse(string1, string2)
is_reverse('FGH','HGF')

