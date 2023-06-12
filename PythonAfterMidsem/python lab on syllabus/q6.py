# Write a program to add and multiply numbers using user define functions.

def sum(num1, num2):
    add = num1+num2
    return add

def product(num1, num2):
    product = num1*num2
    return product

num1 = int(input("Enter 1st number: "))
num2 = int(input("Enter 2nd number: "))

print("sum of the two given numbers are:", sum(num1, num2))
print("product of the two given numbers are:", product(num1, num2))
