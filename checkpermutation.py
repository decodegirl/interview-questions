#write a method to decide if one is a permutation of the other.

def arePermutation(str1, str2): 
      
    # Get lengths of both strings 
    n1 = len(str1) 
    n2 = len(str2) 
  
    # If length of both strings is not same, 
    # then they cannot be Permutation 
    if n1 != n2: 
        return False
  
    # Sort both strings 
    a = sorted(str1) 
    str1 = " ".join(a) 
    # print(a)
    b = sorted(str2) 
    # print(b)
    str2 = " ".join(b) 
  
    # Compare sorted strings 
    for i in range(0, n1, 1): 
        if (str1[i] != str2[i]): 
            return False
  
    return True

# Driver Code 
if __name__ == '__main__': 
    str1 = "test"
    str2 = "estt"
    if (arePermutation(str1, str2)): 
        print("Yes they are") 
    else: 
        print("No they are not permutations") 


#method two using list.sort()

def checkPermutation(s1,s2):
    if len(s1) != len(s2):
        return False
    s1 = list(s1)
    s1.sort()
    s2 = list(s2)
    s2.sort()
    for index in range(len(s1)):
        if s1[index] != s2[index]:
            return False
    return True

print (checkPermutation("abhinaya","aaanbhiy"))
print(checkPermutation("abhinaya","Daanbhiy"))