def partition(lst, start, end):
    pos = start                           # condition was obsolete, loop won't
                                          # simply run for empty range

    for i in range(start, end):           # i must be between start and end-1
        if lst[i] < lst[end]:             # in your version it always goes from 0
            lst[i],lst[pos] = lst[pos],lst[i]
            pos += 1

    lst[pos],lst[end] = lst[end],lst[pos] # you forgot to put the pivot
                                          # back in its place
    return pos

def quick_sort_recursive(lst, start, end):
    if start < end:                       # this is enough to end recursion
        pos = partition(lst, start, end)
        quick_sort_recursive(lst, start, pos - 1)
        quick_sort_recursive(lst, pos + 1, end)
                                          # you don't need to return the list
                                          # it's modified in place

testlist1 = [3,5,6,7,8,9,0,0,3,4,5]
testlist2 = [1,2,3,4,5,6,7,8,9,10]
testlist3 = [10,9,8,7,6,5,4,3,2,1]


example = [3,45,1,2,34]
quick_sort_recursive(example, 0, len(example) - 1)
print(example)