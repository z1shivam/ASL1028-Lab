english = int(input("enter the marks of english:")
math = int(input("enter the marks of math:")
science = int(input("enter the marks of science:")
social = int(input("enter the marks of social studies:")

if english >80 and math>80 and science>80 and social>80:
             print("Stream allocated is science")
elif english>80 and math>50 and science>50:
    print("commerce stram is allocated")
elif english>80 and social>80:
    print("humanities stream is allocated")
else:
    print("invalid input")
