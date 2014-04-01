def count(sequence,item):
    cnt=0
    for c in sequence:
        if str(c) == str(item):
            cnt += 1
    return cnt
    
print count([1,2,1,1],1)
