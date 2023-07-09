from tkinter import *
s = Tk()

s.geometry("600x500")
s.title('I dont know what this is.......!')

l1 = Label(s, text='Hello there!', font=("open sans", 24)).pack()
l2 = Label(s, text='\nDo not press the button below\n', font=("open sans", 12 )).pack(side=LEFT)
b1 =  Button(s, text="do not press",font=('open sans', 18), activebackground='red', activeforeground='white').pack()
l3 = Label(s, text='okay, now i know what to do with this\n i am going to practice all of the widgets here').pack()

c1 = Checkbutton(s, text='This is first checkbox', font=('open sans', 18)).pack()
r1 = Radiobutton(s, text='this is radio button').pack()
lb1 = Listbox(s)
lb1.insert(1, 'shivam')
lb1.insert(2, 'shivam2')
lb1.pack()
e1 = Entry(s).pack()
s.mainloop() 