# WAP to enter marks of a student in five different subjects and calculate the average marks.

# Input the marks of the student
marks1 = float(input("Enter the marks of the student in subject 1: "))
marks2 = float(input("Enter the marks of the student in subject 2: "))
marks3 = float(input("Enter the marks of the student in subject 3: "))
marks4 = float(input("Enter the marks of the student in subject 4: "))
marks5 = float(input("Enter the marks of the student in subject 5: "))
# Calculate the average marks
average = (marks1 + marks2 + marks3 + marks4 + marks5) / 5
# Print the average marks
print("The average marks of the student is", average)