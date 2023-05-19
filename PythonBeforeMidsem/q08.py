# WAP to enter a character. If it is lowercase convert it to uppercase and vice versa

c = input("Enter character: ")
if c.isupper():
    ct = c.lower()
else:
    ct = c.upper()

print("Toggled case =", ct)