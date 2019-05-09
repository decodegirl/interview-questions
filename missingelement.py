import collections


def finder(arr1,arr2):
    d = collections.defaultdict(int)

    for num in arr2:
        d[num] += 1

    for num in arr1:
        if d[num] == 0:
            return num
        else:
            d[num] -= 1


print(finder([1,3,5,7,9,],[1,3,7,9]))


# performing an xor between the numbers in the arrays


def finder3(arr1,arr2):
    result = 0

    for num in arr1 + arr2:
        result ^= num
        print(result)
    return result


print(finder([1,3,5,7,9,],[1,3,7,9]))


# solutin 3

def finder(arr1,arr2):
    arr1.sort()
    arr2.sort()

    for num1,num2 in zip(arr1,arr2):
        if num1 != num2:
            return num1
    return arr1[-1]

print(finder([1,3,5,7,9,],[1,3,7,9]))