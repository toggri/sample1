threes_and_fives = filter(lambda x : x%3==0 or x%5==0, [x for x in range(1,16)])
print threes_and_fives


garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"

message = filter(lambda s: s != 'X',garbled)
print message
