from tkinter import *

root = Tk()
root.geometry("500x600")
root.title("Railway Ticket Form")

title_label = Label(root, text="Railway Ticket Form", font=("Arial Bold", 20), fg="red")
title_label.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

Label(root, text="Name:").grid(row=1, column=0, padx=10, pady=10)
Label(root, text="Day of Traveling:").grid(row=2, column=0, padx=10, pady=10)
Label(root, text="From:").grid(row=3, column=0, padx=10, pady=10)
Label(root, text="To:").grid(row=4, column=0, padx=10, pady=10)
Label(root, text="Train Number:").grid(row=5, column=0, padx=10, pady=10)
Label(root, text="Train Name:").grid(row=6, column=0, padx=10, pady=10)
Label(root, text="Gender:").grid(row=7, column=0, padx=10, pady=10)
Label(root, text="Mobile Number:").grid(row=8, column=0, padx=10, pady=10)

father_name = Entry(root)
father_name.grid(row=1, column=1, padx=10, pady=10)

day_of_traveling = Entry(root)
day_of_traveling.grid(row=2, column=1, padx=10, pady=10)

from_station = Entry(root)
from_station.grid(row=3, column=1, padx=10, pady=10)

to_station = Entry(root)
to_station.grid(row=4, column=1, padx=10, pady=10)

train_number = Entry(root)
train_number.grid(row=5, column=1, padx=10, pady=10)

train_name = Entry(root)
train_name.grid(row=6, column=1, padx=10, pady=10)

gender = StringVar()
male_radio = Radiobutton(root, text="Male", variable=gender, value="Male")
male_radio.grid(row=7, column=1, padx=10, pady=10)

female_radio = Radiobutton(root, text="Female", variable=gender, value="Female")
female_radio.grid(row=7, column=2, padx=10, pady=10)

mobile_number = Entry(root)
mobile_number.grid(row=8, column=1, padx=10, pady=10)

def submit():
    name = father_name.get()
    date = day_of_traveling.get()
    frm = from_station.get()
    to = to_station.get()
    number = train_number.get()
    tname = train_name.get()
    gender_value = gender.get()
    mobile = mobile_number.get()
    message = f"Dear {name}, your train ticket from {frm} to {to} on {date} has been booked.\nTrain Number: {number}\nTrain Name: {tname}\nGender: {gender_value}\nMobile Number: {mobile}"
    output_label.config(text=message)
    
submit_button = Button(root, text="Submit", command=submit, bg="green", fg="white")
submit_button.grid(row=9, column=1, padx=10, pady=10)

def reset():
    father_name.delete(0, END)
    day_of_traveling.delete(0, END)
    from_station.delete(0, END)
    to_station.delete(0, END)
    train_number.delete(0, END)
    train_name.delete(0, END)
    mobile_number.delete(0, END)
    male_radio.deselect()
    female_radio.deselect()
    output_label.config(text="")
    
reset_button = Button(root, text="Reset", command=reset, bg="red", fg="white")
reset_button.grid(row=9, column=2, padx=10, pady=10)

output_label = Label(root, text="", font=("Arial", 9))
output_label.grid(row=10, column=0, columnspan=3, padx=10, pady=10)

root.mainloop()