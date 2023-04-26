#WAP to accept a number from 1-7 and display the name of the day like 1 for sunday, 2 for monday, and so on...

while True:
    a = input("Enter your choice: ")
    b = int(input("Enter any number 1 to 7: "))
    if b == 1:
        print("Sunday"); break
    if b == 2:
        print("Monday"); break
    if b == 3:
        print("Tuesday"); break
    if b == 4:
        print("Wednesday"); break
    if b == 5:
        print("Thursday"); break
    if b == 6:
        print("Friday"); break
    if b == 7:
        print("Saturday"); break
    
    print("Invalid Choice")
    