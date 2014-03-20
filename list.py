# 1
zoo_animals = ["pangolin","cassowary", "sloth", "lion"]

if len(zoo_animals) > 3:
   print "The first animal at the zoo is the "+ zoo_animals[0]
   print "The second animal at the zoo is the "+ zoo_animals[1]
   print "The third animal at the zoo is the "+ zoo_animals[2]
   print "The fourth animal at the zoo is the "+ zoo_animals[3]

# 2
numbers = [5,6,7,8]
print "Adding the numbers at indices 0 and 2..."
print numbers[0] + numbers[2]
print "Adding the numbers at indices 1 and 3..."
print numbers[1] + numbers[3]

# 3
suitcase = [] 
suitcase.append("sunglasses")

suitcase.append("socks")
suitcase.append("watch")
suitcase.append("tai")

list_length = len(suitcase) # Set this to the length of suitcase

print "There are %d items in the suitcase." % (list_length)
print suitcase

# 4
suitcase = ["sunglasses", "hat", "passport", "laptop", "suit", "shoes"]

first  = suitcase[0:2]  # The first and second items (index zero and one)
middle = suitcase[2:4]     # Third and fourth items (index two and three)
last   = suitcase[4:6]     # The last two items (index four and five)
# >>> Notice : Not including the index after the colon.
# >>> Result of "print last" is ["suit", "shoes"] 
print suitcase
print first
print middle,last

# 5 slice
animals = "catdogfrog"
cat  = animals[:3]   # The first three characters of animals
dog  = animals[3:6]  # The fourth through sixth characters
frog = animals[6:]   # From the seventh character to the end

# 6 search
animals = ["aardvark", "badger", "duck", "emu", "fennec fox"]
duck_index = animals.index("duck") # Use index() to find "duck"

animals.insert(duck_index,"cobra")
print animals # Observe what prints after the insert operation

# 7 remove list items
animals.remove('badger')
print "removed 'badger' " 
print animals
