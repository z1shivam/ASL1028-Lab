class student:
    def __init__(self,name,college):
        self.name = name
        self.college = college

    def printdetails(self):
        print(f"{self.name} is a student of {self.college}")

shivam = student("Pranav","cse")
shivam.printdetails()
