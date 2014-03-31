def is_prime(x):
    if x == 0 or x == 1 or x < 0:
        return False
    elif x == 2:
        return True
    else:
        for n in range(2,x-1):
            if x%n == 0:
                return False
                break
    return True
print "5 is prime. : ",is_prime(5)
print "8 is prime. : ",is_prime(8)
print is_prime(-10)
print is_prime(0)
print is_prime(1)
print is_prime(2)
print is_prime(3)
print is_prime(4)
print is_prime(5)
