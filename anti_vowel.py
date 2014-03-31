def anti_vowel(text):
    ptn = "aeiouAEIOU"
    result = ""
    for c in text:
        print c,
        if c not in ptn:
            result = result + c
    return result
    
print anti_vowel("Hey You!")
