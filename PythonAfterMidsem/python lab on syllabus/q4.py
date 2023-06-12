# Write a program to print table of a number.

num = int(input("Enter the number for table:"))
for i in range(1,11):
    print("\t",num, "x", i,"=",num*i)