# size = int(input("Enter the size of the diamond: "))
size = 5
def hollow_diamond():
    for i in range(0,size):
        print(" "*(size-i) + "*" + " "*(2*i - 1) + "*"*(i != 0))

    for i in range(size,-1,-1):
        print(" "*(size-i) + "*" + " "*(2*i - 1) + "*"*(i != 0))

def filled_diamond():
    for i in range(0, size):
        print(" "*(size-i) + "* "*i)

    for i in range(size, -1,-1):
        print(" "*(size-i) + "* "*i)


def num_pyramid():
    for j in range(0,size+1):   
        print(" "*j,end="") 
        for i in range(j,size):
            print(i, end="")
        for i in range(size,j-1,-1):
            print(i, end="")
        print("\n", end="")

