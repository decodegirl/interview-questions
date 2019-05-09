# An anagram is when the two strings can be written using the exact same letters
def anagram(str1,str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    #edge case of letters
    if len(str1) != len(str2):
        return False

    count = {}

    for letter in str1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1

    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1

    for j in count:
        if count[j] != 0:
            return False
    return True

print(anagram("dog","god"))
print(anagram("life","man"))

