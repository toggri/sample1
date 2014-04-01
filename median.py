def median(nlist):
    if len(nlist)==1:
        return nlist[0]
        
    sorted_list = sorted(nlist)
    if len(sorted_list)%2 == 0:
        return float(float(sorted_list[len(sorted_list)/2-1]+sorted_list[len(sorted_list)/2])/2)
    else:
        return sorted_list[(len(sorted_list)+1)/2-1]

print median([2,1])
print median([7,3,1,4])
print median([3,5,2])
print median([1,1,2])
print median([1])
