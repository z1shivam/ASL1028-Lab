'''Write a program to print following pattern: 
0 
01 
012'''

for i in range(0,3):
    for j in range(0, i+1):
        print(j,end='')
    print()