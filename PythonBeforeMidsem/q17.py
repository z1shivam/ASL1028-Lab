num = int(input("Enter a number: "))
last_digit = num%10

if last_digit%3==0:
    print("the last digit of the number is divisible by 3")
else:
    print("The last digit is not divisible by 3")
    
