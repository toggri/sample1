s="this hack is wack hack"

list=s.split()

print list

def censor(text,word):
    slist = text.split()
    result = []
    for sword in slist:
        if sword == word:
            result.append("*"*len(sword))
        else:
            result.append(sword)
    print result
    return " ".join(result)

print censor(s,"hack")
