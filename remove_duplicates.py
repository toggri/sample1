def remove_duplicates(nlist):
    ns = []
    for i in nlist:
        if i not in ns:
            ns.append(i)
    return ns

print remove_duplicates([1,2,1,2,1,2,3,4,3,4])
