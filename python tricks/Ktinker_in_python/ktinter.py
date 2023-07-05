from tkinter import *

def clickevent():
    btntxt.configure(text="dear "+nameentry.get()+", Info submitted")

mywindow = Tk()
mywindow.title('My first GUI application')
mywindow.geometry('350x150')

toplabel = Label(mywindow, text='Welcome Beautiful People')
namelabel = Label(mywindow, text='Enter your name: ')
scllabel = Label(mywindow, text='Enter your department: ')
btntxt = Label(mywindow, text='')

nameentry = Entry(mywindow, width= 15)
sclentry = Entry(mywindow, width=15)

submitbtn = Button(mywindow, text='submit now', width= 20, command=clickevent)

toplabel.grid(column=0, row=0)
toplabel.pack()
namelabel.grid(column=0, row=1)
scllabel.grid(column=0, row=2)
btntxt.grid(column=0, row=4)

nameentry.grid(column=1, row=1)
sclentry.grid(column=1, row=2)

submitbtn.grid(column=0, row=3)

mywindow.mainloop()