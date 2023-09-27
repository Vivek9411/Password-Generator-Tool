import tkinter
import pyperclip
from tkinter import messagebox
from generatepassword import PasswordGenerator
Email = 'harry6@gmail.com'
# ---------------------------- PASSWORD GENERATOR ------------------------------- #\



def output_password():
    password_entry.delete(0, tkinter.END)
    password_generated = PasswordGenerator()
    pyperclip.copy(password_generated.password)
    password_entry.insert(0, string=password_generated.password)

# ---------------------------- SAVE PASSWORD ------------------------------- #



def add_button():
    website_name = website_entry.get()
    email_name = email_entry.get()
    password_name = password_entry.get()

    if len(website_name) == 0 or len(email_name) == 0 or len(password_name) == 0:
        messagebox.showerror(title='error', message="every field should be filled")
    else:
        message = messagebox.askyesno(title=website_name, message=f"email: {email_name}\n password: {password_name}")
        if message:
            with open(file='123.txt', mode='a') as file:
                file.write(f"{website_name} | {email_name}   |  {password_name}\n")
            website_entry.delete(0, tkinter.END)
            password_entry.delete(0, tkinter.END)


# ---------------------------- UI SETUP ------------------------------- #

window = tkinter.Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

lock_image = tkinter.PhotoImage(file="logo.png")

canvas = tkinter.Canvas(width=200, height=200)
canvas.create_image(100, 100, image=lock_image)
canvas.grid(row=0, column=1)



# labels
# web_sites

websites = tkinter.Label(text='website:', pady=10, padx=20)
websites.grid(column=0, row=1)

email_username = tkinter.Label(text='Email/Username:', pady=10, padx=20)
email_username.grid(column=0, row=2)

password = tkinter.Label(text='Password', pady=10, padx=20)
password.grid(column=0, row=3)

website_entry = tkinter.Entry(width=40)
website_entry.focus()
website_entry.grid(column=1, row=1, columnspan=2)

email_entry = tkinter.Entry(width=40)
email_entry.insert(0, string=Email)
email_entry.grid(column=1, row=2, columnspan=2)



password_entry = tkinter.Entry(width=25)
password_entry.grid(column=1, row=3)

# button

generate_password = tkinter.Button(text='Generate password', width=17, font=('Arial', 8, ),command=output_password)
generate_password.grid(column=2, row=3)

add = tkinter.Button(text='Add', width=40, command=add_button)
add.grid(columnspan=2, column=1, row=4)
tkinter.mainloop()
