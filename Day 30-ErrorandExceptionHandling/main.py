import json
from tkinter import *
from tkinter import messagebox
import pyperclip
import random



# ---------------------------- PASSWORD GENERATOR ------------------------------- #
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']


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
    new_data = {
        web_entry: {
            "email": email_entry,
            "password": pw_entry,
        }
    }
    if len(web_entry) == 0 or len(pw_entry) == 0:
        messagebox.showinfo(title="ERROR", message="Website and Password Fields cannot be empty.")
    else:
        try:
            with open("data.json", "r") as log:
                data = json.load(log)

        except FileNotFoundError:
            with open("data.json", "w") as log:
                json.dump(new_data, log, indent=4)
                messagebox.showinfo(title="Success", message="Password saved successfully")

        else:
            data.update(new_data)
            with open("data.json", "w") as log:
                json.dump(data, log, indent=4)
                messagebox.showinfo(title="Success", message="Password saved successfully")
        finally:
            clear_screen()


# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search_password():
    query = website_textfield.get()
    try:
        with open("data.json", "r") as log:
            data = json.load(log)
    except FileNotFoundError:
        messagebox.showinfo(title="No File", message="No Password File has been created.")
        clear_screen()
    else:
        if query in data:
            email = data[query]["email"]
            password = data[query]["password"]
            messagebox.showinfo(title=query, message=f"email: {email}\npassword: {password}")
            clear_screen()
        else:
            messagebox.showinfo(title="No Entry Found", message=f"{query} not found in Manager.")
            clear_screen()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50)


def clear_screen():
    website_textfield.delete(0, END)
    password_textfield.delete(0, END)
    website_textfield.focus()


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

website_textfield = Entry(width=32)
website_textfield.grid(row=1, column=1)
website_textfield.focus()
userinfo_textfield = Entry(width=32)
userinfo_textfield.grid(row=2, column=1)
userinfo_textfield.insert(END, "sergio@example.com")
password_textfield = Entry(width=32)
password_textfield.grid(row=3, column=1)

generate_pw_button = Button(text="Generate Password", command=gen_password)
generate_pw_button.grid(row=3, column=2)
add_pw_button = Button(text="Add", width=44, command=save_password)
add_pw_button.grid(row=4, column=1, columnspan=2)
search_pw_button = Button(text="Search", width=14, command=search_password)
search_pw_button.grid(row=1, column=2)

window.mainloop()

