from tkinter import *
from tkinter import messagebox
import pyperclip
import random
from options_pool import *


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def gen_password():
    pw_letters = [random.choice(letters) for _ in range(1, 9)]
    pw_symbols = [random.choice(symbols) for _ in range(1, 5)]
    pw_numbers = [random.choice(numbers) for _ in range(1, 5)]

    password_list = pw_letters + pw_symbols + pw_numbers
    random.shuffle(password_list)
    password = "".join(password_list)

    password_textfield.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save_password():
    web_entry = website_textfield.get()
    email_entry = userinfo_textfield.get()
    pw_entry = password_textfield.get()

    if len(web_entry) == 0 or len(pw_entry) == 0:
        messagebox.showerror(title="ERROR", message="Website and Password Fields cannot be empty.")
        return
    if ".com" not in email_entry:
        messagebox.showerror(title="ERROR", message="Must enter a valid email.")
        return

    accept = messagebox.showinfo(title=web_entry, message=f"Are you sure you want to save these details? "
                                                          f"\nEmail: {email_entry} \nPassword: {pw_entry}")

    if accept:
        with open("data.txt", "a") as log:
            log.write(f"{web_entry}  |  {email_entry}  |  {pw_entry}\n")
            website_textfield.delete(0, END)
            website_textfield.focus()
            password_textfield.delete(0, END)
        messagebox.showinfo(title="Success", message="Password saved successfully")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)

canvas = Canvas(height=200, width=200)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:")
website_label.grid(row=1, column=0)
user_info_label = Label(text="Email/Username:")
user_info_label.grid(row=2, column=0)
password_label = Label(text="Password:")
password_label.grid(row=3, column=0)

website_textfield = Entry(width=35)
website_textfield.grid(row=1, column=1, columnspan=2)
website_textfield.focus()
userinfo_textfield = Entry(width=35)
userinfo_textfield.grid(row=2, column=1, columnspan=2)
userinfo_textfield.insert(END, "sergio@example.com")
password_textfield = Entry(width=17)
password_textfield.grid(row=3, column=1)

generate_pw_button = Button(text="Generate Password", command=gen_password)
generate_pw_button.grid(row=3, column=2)
add_pw_button = Button(text="Add", width=35, command=save_password)
add_pw_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
