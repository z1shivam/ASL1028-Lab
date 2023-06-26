def max_finder(int1, int2, int3):
    list1 = [int1, int2, int3]
    maxm = max(list1)
    return maxm

int1 = int(input("Enter a number: "))
int2 = int(input("Enter 2nd number: "))
int3 = int(input("Enter 3rd number: "))

print("The maximum of the numbers is: ",max_finder(int1, int2, int3))
