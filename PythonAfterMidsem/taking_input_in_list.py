list1=[]
n = int(input("Enter number of elements: "))

for i in range(n):
    print("Enter the value of element",i+1,":")
    v = int(input())
    list1.append(v)
print(list1)