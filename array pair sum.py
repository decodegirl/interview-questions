# Given an integer array, output all the unique pairs that sum up to a specific value k.

def pair_sum(arr,k):

    if len(arr) < 2:
        return

    seen = set()
    output = set()
    for num in arr:

        target = k - num
        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num,target)),max(num,target)))

    ##trick to print the two pairs as a tuple
    print("\n".join(map(str,list(output))))

pair_sum([1,3,2,2],4)
