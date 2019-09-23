## when you add a string to itself, all the rotations of the original string will be a 
# substring to that mdofied version of the string. check it :)

def isSubstring(s1, s2):
    return s2 in s1
    
def checkRotation(s1, s2):

    if len(s1) == len(s2) and len(s1) > 0:
        return isSubstring(s1+s1,s2)
        
    return False

print(checkRotation('waterbottle', 'erbottlewat'))