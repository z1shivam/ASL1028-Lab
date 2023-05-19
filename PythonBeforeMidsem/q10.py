# WAP to accept a number from 1 to 12 and display the name of the month and days in that month, like 1 for January and the number of days and so on

while True:
    n = int(input("Enter month number: "))
    if 1 <= n <= 12:
        print("Corresponding month =", ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"][n - 1])
        print("\t& no. of days =", [31, "28 or 29", 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][n - 1])
        break
    print("Invalid number!")