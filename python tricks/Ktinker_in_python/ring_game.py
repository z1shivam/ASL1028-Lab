from tkinter import *

new_window = Tk()
new_window.title('RING RING GAME')
new_window.geometry('320x150')

button1 = Button(text='Playing with buttons',bg='red',fg='white')
button1.pack(side='top',fill='both',expand=True)

button2 = Button(text='Playing with buttons',bg='blue',fg='white')
button2.pack(side='top',fill='both',expand=True)

button3 = Button(text='Playing with buttons',bg='green',fg='white')
button3.pack(side='top',fill='both',expand=True)

new_window.mainloop()