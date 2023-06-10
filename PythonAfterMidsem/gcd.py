def findgcd(num1, num2):
    if num1==0:
        return num2
    elif num2==0:
        return num1
    else:
        if num1>=num2:
            return findgcd(num2,num1%num2)
        else:
            return findgcd(num1,num2%num1)
    
print(findgcd(5,2))