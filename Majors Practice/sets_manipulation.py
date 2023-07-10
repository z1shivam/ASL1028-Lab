my_set = {1, 2, 3, 4, 5}

# Adding and Removing Elements
my_set.add(6)
print(my_set)              # Output: {1, 2, 3, 4, 5, 6}

my_set.update({7, 8, 9})
print(my_set)              # Output: {1, 2, 3, 4, 5, 6, 7, 8, 9}

my_set.remove(3)
print(my_set)              # Output: {1, 2, 4, 5, 6, 7, 8, 9}

my_set.discard(4)
print(my_set)              # Output: {1, 2, 5, 6, 7, 8, 9}

popped = my_set.pop()
print(popped)              # Output: 1

# Set Operations
new_set = my_set.union({6, 7})
print(new_set)             # Output: {2, 5, 6, 7, 8, 9}

new_set = my_set.intersection({3, 4, 5})
print(new_set)             # Output: {5}

new_set = my_set.difference({4, 5, 6})
print(new_set)             # Output: {2}

new_set = my_set.symmetric_difference({4, 5, 6})
print(new_set)             # Output: {2, 6}

# Useful Set Functions
length = len(my_set)
print(length)              # Output: 7

new_set = my_set.copy()
print(new_set)             # Output: {2, 5, 6, 7, 8, 9}
