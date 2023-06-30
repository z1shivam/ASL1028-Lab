import time

def grade(num):
    if num>=90: return 'A' 
    if num>=80: return 'A-'
    if num>=70: return 'B'
    if num>=60: return 'B-'
    if num>=50: return 'C'
    if num>=40: return 'C-'
    return 'F'

num = float(input("Enter your marks: "))
time.sleep(1)
print(grade(num))
