num1=int(input("Enter a number: "))
num2=int(input("Enter second number: "))
op = input("enter a operation")

if op =='+':
    result=num1+num2
if op == '-':
    result = num1-num2
if op == '*':
    result = num1*num2
if op == '\\':
    result = num1/num2

print("the result is", result)
         
