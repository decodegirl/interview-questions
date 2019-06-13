def compress(s):
    """
    This solution compresses without checking. Known as the RunLength Compression algorithm.
    """

    # Begin Run as empty string
    r = ""
    l = len(s)

    # Check for length 0
    if l == 0:
        return ""

    # Check for length 1
    if l == 1:
        return s + "1"

    # Intialize Values
    last = s[0]
    cnt = 1
    i = 1

    while i < l:

        # Check to see if it is the same letter
        if s[i] == s[i - 1]:
            # Add a count if same as previous
            cnt += 1
        else:
            # Otherwise store the previous data
            r = r + s[i - 1] + str(cnt)
            cnt = 1

        # Add to index count to terminate while loop
        i += 1

    # Put everything back into run
    r = r + s[i - 1] + str(cnt)

    return r

print(compress('AAABBCCCCDDD'))