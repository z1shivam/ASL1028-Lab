number = int(input("Enter a number: "))

if number >= 0 and number <= 9:
    print("The number is a one digit number.")
elif number >= 10 and number <= 99:
    print("The number is a two digit number.")
elif number >= 100 and number <= 999:
    print("The number is a three digit number.")
else:
    print("The number is a more than three digit number.")
