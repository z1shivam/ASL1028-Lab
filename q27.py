# wap to check for leap year

year = int(input("Enter the year to check: "))
if year%4 == 0 and (year%100!=0 or year%400==0):
    print(year, "is a leap year")
else:
    print("Year is not leap")