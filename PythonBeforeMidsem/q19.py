side1= int(input("enter the length of side1:"))
side2= int(input("enter the length of side2:"))
side3= int(input("enter the length of side3:"))

if side1==side2==side3:
    print("The triangle is equilateral")
elif side1==side2 or side1==side3 or side2==side3:
    print("The triangle is isosceles")
else:
    print("The triangle is scelene")
    

