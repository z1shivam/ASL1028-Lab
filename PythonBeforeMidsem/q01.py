# write a program to find the sum of the digit of a five digit number

num = int(input("Enter a five digit number"))

# extracting the digits
a = num%10
num //= 10

b = num%10
num //= 10

c = num%10
num //= 10

d = num%10
num //= 10

e = num%10
num //= 10

print("The sum of the digit is ",(a+b+c+d+e))

print("Checking a feature")