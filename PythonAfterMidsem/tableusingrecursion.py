def printtable(num):
    for i in range(1,11):
        print(num,"x",i, "=", num*i)

num = int(input("Enter a number to print a table: "))
printtable(num)