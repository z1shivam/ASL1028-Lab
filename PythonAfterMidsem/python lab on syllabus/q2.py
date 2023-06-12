# Write a program to calculate grade of a student.

marks = int(input("Enter the marks of the student: "))

if marks > 90 and marks <=100:
    grade = 'A'

elif marks > 80 and marks <=90:
    grade = 'B'

elif marks > 70 and marks <=80:
    grade = 'C'

elif marks > 60 and marks <=70:
    grade = 'D'

elif marks > 0 and marks <= 60:
    grade = 'fail'

else:
    grade = 'Enter a valid marks value.'

print("Grade of the student is:", grade)