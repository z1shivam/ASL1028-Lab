# WAP to swap the values of two variables

value1 = input("Enter the value of the first variable: ")
value2 = input("Enter the value of the second variable: ")

temp = value1
value1 = value2
value2 = temp

print("The new value of the first variable is: ", value1)
print("The new value of the second variable is: ", value2)