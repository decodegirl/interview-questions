# Returns true if edit distance between s1 and s2 is
# one, else false
def isEditDistanceOne(s1, s2):
    # Find lengths of given strings
    m = len(s1)
    n = len(s2)

    # If difference between lengths is more than 1,
    # then strings can't be at one distance
    if abs(m - n) > 1:
        return False

    count = 0  # Count of isEditDistanceOne

    i = 0
    j = 0
    while i < m and j < n:
        # If current characters dont match
        if s1[i] != s2[j]:
            if count == 1:
                return False

                # If length of one string is
            # more, then only possible edit
            # is to remove a character
            if m > n:
                i += 1
            elif m < n:
                j += 1
            else:  # If lengths of both strings is same
                i += 1
                j += 1

            # Increment count of edits
            count += 1

        else:  # if current characters match
            i += 1
            j += 1

    # if last character is extra in any string
    if i < m or j < n:
        count += 1

    return count == 1


print(isEditDistanceOne("pale", "ple"))
print(isEditDistanceOne("pales", "pale"))
print(isEditDistanceOne("pale", "bale"))
print(isEditDistanceOne("pale", "bake"))

#solution 2

def is_one_away(string1, string2):
    longer, shorter = ([string1, string2] if len(string1) >= len(string2)
                       else [string2, string1])
    edits_away = 0
    if len(longer) == len(shorter):
        for i in range(len(longer)):
            if longer[i] != shorter[i]:
                edits_away += 1
            if edits_away == 2:
                return False
        return True
    elif len(longer) - len(shorter) == 1:
        for i in range(len(longer)):
            if i - edits_away >= len(shorter):
                edits_away += 1
            elif longer[i] != shorter[i - edits_away]:
                edits_away += 1
            if edits_away == 2:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    first_word = input("First Word? ")
    second_word = input("Second Word? ")
    print(is_one_away(first_word,second_word))


#solution 3
def oneAway(s1,s2):
    if abs(len(s1)-len(s2)) > 1:
        return False
    if len(s1) > len(s2):   
        smallS,bigS = s2,s1
    else:
        smallS,bigS = s1,s2
    sIndex = 0
    bIndex = 0
    firstError = False
    while sIndex < len(smallS):
        if smallS[sIndex] == bigS[bIndex]:
            sIndex += 1
            bIndex += 1
        elif firstError == False:
            firstError = True
            if len(s1) == len(s2):
                sIndex += 1
                bIndex += 1
            else:
                bIndex += 1
        else:
            return False
    return True


print(oneAway("pale", "ple"))
print(oneAway("pales", "pale"))
print(oneAway("pale", "bale"))
print(oneAway("pale", "bake"))