str = input("Enter a string")
str = str.lower()           

if str == str[::-1]:
    print("string is pallindrome")

else:
    print("the string is not a pallindrome")
