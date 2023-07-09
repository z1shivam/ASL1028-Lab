from tkinter import *

s = Tk()
s.title('Divorce Form')
s.geometry('600x700')

l1 = Label(s, text="Husband's Name:\t").grid(row=1, column=1)
e1 = Entry(s).grid(row=1, column=2)

l2 = Label(s, text="Wife's Name:\t").grid(row=2, column=1)
e2 = Entry(s).grid(row = 2, column=2)



s.mainloop()