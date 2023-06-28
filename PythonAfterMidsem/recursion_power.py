num = int(input("Enter the number: "))
power = int(input("Enter the power: "))

#using lambda function:
print((lambda x,y : x**y)(num, power))

#using resursion function:
def powerr (num, power):
    if power == 0:
        return 1
    else:
        result = 1
        result = num * powerr(num,power-1)
        return result
print(powerr(num, power))

# using normal function:
def powerf (num, power):
    return num**power
print(powerf(num, power))