my_list = range(16)
print filter(lambda x: x % 3 == 0, my_list)

squares = [x*x for x in range(1,11)]
print squares
print filter(lambda x: 30 < x <= 70, squares)
