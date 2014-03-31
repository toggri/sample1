def reverse(text):
    cnt_text = len(text)-1
    result = ""
    while cnt_text >= 0:
        result = result + text[cnt_text]
        cnt_text -= 1
    return result

print reverse("abcd")
        
