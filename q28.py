# wap to check if a string contain a certain character

string = input("enter a string: ")
char = input("Enter a character to search: ")

if char in string:
    print("The string contains the character")
else: 
    print("The string does not contain the character")