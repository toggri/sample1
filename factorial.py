def factorial(x):
    if x < 0:
        return x," is negative integer."
    result = 1
    while x >= 1:
        result = result * x
        x -= 1
    return result
print factorial(4)
