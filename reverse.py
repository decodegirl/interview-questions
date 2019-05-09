# Write a program (using functions!) that asks the user for a long string
# containing multiple words. Print back to the user the same string,
# except with the words in backwards order. For example, say I type the string:


test1 = input("Enter a word of your choice:")


def reverse_word(y):
    return ' ' . join(y.split()[::-1])


print(reverse_word(test1))


# method 2
def reverse_v3(x):
    y = x.split()
    return " ".join(reversed(y))


print(reverse_v3(test1))



# method 3
def reverse_v4(x):
    y = x.split()
    y.reverse()
    return " ".join(y)


print(reverse_v4(test1))