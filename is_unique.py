#solution 1.

def is_unique(s):
    string = s.lower()
    return len(string) == len(set(string))

print(is_unique('Celiny'))

#solution 2. uses hashtable

def is_unique(s):
    #lengh of string should not be greater than 256
    if len(s) > 256:
        return False
    else:
        char_set = {}
        for i in s:
            if i in char_set:
                return False
            
            
            else:
                char_set[i] = True
    return True

s = input('Enter a string:')
print(is_unique(s))