 # Write a method to replace all spaces in a string with '%20'. 
 # You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the "true" length of the string.

def ur_Lify(string, len_str):
    return string[:len_str].replace(' ', '%20')

print(ur_Lify("Mr John Smith     ", 13))

# best solution
def urlify(string,length):
    charArr = list(string)
    j = len(charArr)-1
    for i in range(length-1,-1,-1):
        if(charArr[i]!=' '):
            charArr[j] = charArr[i]
            j -= 1
        else:
            charArr[j] = '0'
            charArr[j-1] = '2'
            charArr[j-2] = '%'
            j -= 3
    return "".join(charArr)

print(urlify("Mr John Smith    ", 13))
# Traverse backwards from the last letter (not space) of your 'array'. 
# Whenever you hit a letter, move it to the last space in the array. 
# If a space is found, there will now be enough space to add "%20." 
# Do it one character at a time, and continue the loop until you reach index 0.

# Time and Space Complexity: Both O(n).



def URLify(s,trueLength):
    s = list(s)
    # flag = False
    trueSpaceCount = 0
    for char in range(0,trueLength):
        if s[char] == " ":
            trueSpaceCount += 1
    finalLength = trueLength + 2*trueSpaceCount #each space is replaced by %20 in final string
    #addition of 2 more characters for each space
    for char in range(trueLength-1,-1,-1):
        if s[char] != " ":
            s[finalLength-1] = s[char]
            finalLength -= 1
        else:
            s[finalLength-3:finalLength] = ["%","2","0"]
            finalLength -= 3
    return "".join(s)
print(URLify("Mr John Smith    ",13))