def digit_sum(n):
    print n
    result = 0
    for c in str(n):
        result = result + int(c)
    return result

print digit_sum(1234)
