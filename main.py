from os import write
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle

from pandas.core.computation.align import align_terms

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_list_letter = [choice(letters) for _ in range(randint(8, 10))]
    password_list_symbol = [choice(symbols) for _ in range(randint(2, 4))]
    password_list_number = [choice(numbers) for _ in range(randint(2, 4))]
    password_list = password_list_letter+password_list_symbol+password_list_number
    shuffle(password_list)

    password = "".join(password_list)

    password_entry.insert(0, f"{password}")

def add():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()
    if len(website_name)==0 or len(email_name)==0 or len(password_name)==0:
        warning_msg = messagebox.showwarning(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website_name, message=f"These are the details entered: \nEmail: {email_name}\nPassword: {password_name}\nIs it okay to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website_name} | {email_name} | {password_name}\n")
            website_entry.delete(0, END)
            email_entry.delete(0, END)
            password_entry.delete(0, END)

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(width=200, height=200)
img = PhotoImage(file="logo.png")
canvas.create_image(125,100,image=img)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)

website_entry = Entry(width=35)
website_entry.grid(row=1, column=1, columnspan=2)
website_entry.focus()

email_label = Label(text="Email/Username:")
email_label.grid(column=0, row=2)

email_entry = Entry(width=35)
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:")
password_label.grid(column=0, row=3)

password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

password_button = Button(text="Generate Password", command= gen_password)
password_button.grid(column=2, row=3)

add_button = Button(text="Add", width=36, command=add)
add_button.grid(column=1, row=4, columnspan=2)

window.mainloop()