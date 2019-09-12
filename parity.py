#computing the parity of a word.
# the parity of a binary word is 1 if the number of ones in the word is odd. Otherwise it is 0.

def parity(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

print(parity(100111))