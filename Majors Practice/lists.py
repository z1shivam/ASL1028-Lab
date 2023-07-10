my_list = [1, 2, 3, 4, 5]

# Accessing List Elements
print(my_list[0])          # Output: 1
print(my_list[-1])         # Output: 5
print(my_list[1:4])        # Output: [2, 3, 4]

# Modifying Lists
my_list[0] = 10
print(my_list)             # Output: [10, 2, 3, 4, 5]

my_list.append(6)
print(my_list)             # Output: [10, 2, 3, 4, 5, 6]

my_list.extend([7, 8, 9])
print(my_list)             # Output: [10, 2, 3, 4, 5, 6, 7, 8, 9]

my_list.insert(3, 10)
print(my_list)             # Output: [10, 2, 3, 10, 4, 5, 6, 7, 8, 9]

my_list.remove(3)
print(my_list)             # Output: [10, 2, 10, 4, 5, 6, 7, 8, 9]

del my_list[0]
print(my_list)             # Output: [2, 10, 4, 5, 6, 7, 8, 9]

# List Operations
new_list = my_list + [6, 7]
print(new_list)            # Output: [2, 10, 4, 5, 6, 7]

repeated_list = my_list * 2
print(repeated_list)       # Output: [2, 10, 4, 5, 2, 10, 4, 5]

# Useful List Methods
length = len(my_list)
print(length)              # Output: 8

index = my_list.index(4)
print(index)               # Output: 2

count = my_list.count(5)
print(count)               # Output: 1

my_list.sort()
print(my_list)             # Output: [2, 4, 5, 6, 7, 8, 9, 10]

my_list.reverse()
print(my_list)             # Output: [10, 9, 8, 7, 6, 5, 4, 2]

new_list = my_list.copy()
print(new_list)            # Output: [10, 9, 8, 7, 6, 5, 4, 2]
