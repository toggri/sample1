def purify(numbers):
    nlist = []
    for n in numbers:
        if n%2 == 0:
            nlist.append(n)
    return nlist

print purify([1,2,3,4,5,6,7,8,9])
