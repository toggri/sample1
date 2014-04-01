def censor(text,word):
    slist = text.split()
    result = []
    for sword in slist:
        if sword == word:
            result.append("*"*len(sword))
        else:
            result.append(sword)
    return " ".join(result)
    
a=censor("this hack is wack hack","hack")
print a  
