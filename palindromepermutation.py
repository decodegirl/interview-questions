def PalindromePermutation(s):
    charCounts = dict()
    for char in s:
        if char.lower() in charCounts: 
            charCounts[char.lower()] += 1
        else:
            charCounts[char.lower()] = 1
    countOdds = 0
    for i in charCounts:
        if i != " " and charCounts[i]%2 != 0:
            if countOdds == 1: #this is where you encounter one more odd count character
                return False
            countOdds += 1
    return True
print(PalindromePermutation("Tact Coa"))