size = int(input("Enter the size of the diamond: "))

for i in range(0,size):
    print(" "*(size-i) + "*" + " "*(2*i - 1) + "*"*(i != 0))

for i in range(size,-1,-1):
    print(" "*(size-i) + "*" + " "*(2*i - 1) + "*"*(i != 0))
    