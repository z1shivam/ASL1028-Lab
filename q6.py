# WAP to find the roots of the quadratic equation

a = int(input("Enter the coefficient of x^2: "))
b = int(input("Enter the coefficient of x: "))
c = int(input("Enter the constant term: "))

d = b ** 2 - 4 * a * c

root1 = (-b + d ** 0.5) / (2 * a)
root2 = (-b - d ** 0.5) / (2 * a)