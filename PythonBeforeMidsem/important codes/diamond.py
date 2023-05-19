# Define the size of the diamond
size = 5

# Upper half of the diamond
for i in range(size):
    for j in range(size - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()

# Lower half of the diamond
for i in range(size - 2, -1, -1):
    for j in range(size - i - 1):
        print(" ", end="")
    for j in range(2 * i + 1):
        print("*", end="")
    print()
