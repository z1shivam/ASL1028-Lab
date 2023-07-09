def sum(num):
    length = len(str(num))
    digitsum = 0
    for i in range(0,length):
       
        digitsum += num%10
        num = num//10
    return digitsum


print(sum(33411))